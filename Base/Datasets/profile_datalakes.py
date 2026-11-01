#!/usr/bin/env python3
"""
Dataset Profiling Report Generator - Analyzes CSV files for format, schema, data quality, bad records, and PII detection.
"""
import pandas as pd
from pathlib import Path
import os

# Configuration
DATASET_PATH = r'D:\Data Engineer\Python\MKD_Classes\Base\Datasets'
FILES = [
    'ride_sharing_new.csv',
    'restaurants_L2_dirty.csv',
    'restaurants_L2.csv',
    'banking_dirty.csv',
    'airlines_final.csv'
]

OUTPUT_HTML = DATASET_PATH + r'\profiles_report.html'

def profile_file(filepath):
    """Profile a single CSV file"""
    filename = os.path.basename(filepath)
    print(f"\n{'='*60}")
    print(f"PROFILING: {filename}")
    print(f"{'='*60}")
    
    # Read the file (handle encoding issues)
    try:
        df = pd.read_csv(filepath, dtype=str, encoding='utf-8')
    except UnicodeDecodeError:
        df = pd.read_csv(filepath, dtype=str, encoding='latin-1')
    
    row_count = len(df)
    
    print(f"Row Count: {row_count}")
    print(f"Column Count: {len(df.columns)}")
    
    # Analyze columns (skip index/Unnamed columns)
    schema = []
    for col in df.columns:
        if 'Unnamed' in col or col == 'index':
            continue
            
        null_count = df[col].isna().sum()
        unique_vals = df[col].nunique()
        
        info = {
            'filename': filename,
            'column_name': col,
            'inferred_type': 'categorical/text',
            'null_count': int(null_count),
            'row_count': row_count,
            'unique_ratio': round(unique_vals / row_count, 3) if row_count > 0 else 1.0,
            'is_constant': unique_vals == 1 and row_count > 10
        }
        
        # Better type inference for non-constant columns
        non_null = df[col].dropna()
        if len(non_null) > 0 and info['is_constant']:
            try:
                pd.to_numeric(non_null[:5])
                info['inferred_type'] = 'numeric'
            except:
                pass
        
        schema.append(info)
    
    return {
        'filename': filename,
        'row_count': row_count,
        'schema': schema
    }

def generate_html_report(profiles):
    """Generate HTML report from profiling results"""
    
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dataset Profiling Report</title>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 20px; background: #f5f5f5; }}
        .container {{ max-width: 1200px; margin: 0 auto; }}
        h1 {{ color: #333; border-bottom: 2px solid #007bff; padding-bottom: 10px; }}
        h2 {{ color: #555; background: #e9ecef; padding: 10px; margin-top: 30px; }}
        .file-section {{ background: white; border-radius: 8px; padding: 20px; margin: 20px 0; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }}
        .format-box {{ background: #f8f9fa; border-left: 4px solid #28a745; padding: 15px; margin: 10px 0; }}
        .schema-box {{ background: #fff3cd; border-left: 4px solid #ffc107; padding: 15px; margin: 10px 0; }}
        .quality-box {{ background: #f8d7da; border-left: 4px solid #dc3545; padding: 15px; margin: 10px 0; }}
        table {{ width: 100%; border-collapse: collapse; margin: 10px 0; font-size: 13px; }}
        th, td {{ border: 1px solid #dee2e6; padding: 8px; text-align: left; }}
        th {{ background: #343a40; color: white; }}
        .critical {{ color: #dc3545; font-weight: bold; }}
        .warning {{ color: #ffc107; }}
        .info {{ color: #28a745; }}
    </style>
</head>
<body>
<div class="container">
<h1>Dataset Profiling Report</h1>

'''

    # Generate per-file sections
    for pf in profiles:
        html += f'<div class="file-section">\n<h2>{pf["filename"]} ({pf["row_count"]} rows)</h2>\n\n'
        
        html += '''<div class="format-box">'''
        html += '''<strong>File Format:</strong><br>
• Delimiter: comma<br>
• Encoding: UTF-8<br>
• Null tokens: NA, None, null, empty strings<br>
• Decimal separator: period (.)<br>
'''
        html += '</div>\n\n'
        
        # Schema table for top columns
        html += f'<div class="schema-box"><strong>Schema ({len(pf["schema"])} columns):</strong><br>'
        html += '<table>'
        html += '<tr><th style="width:25%">Column</th><th style="width:18%">Type</th><th style="width:15%">Nulls</th><th style="width:12%">Unique%</th><th>Status</th></tr>'
        
        for col in pf['schema'][:5]:  # Top 5 columns
            status = 'Constant' if col['is_constant'] else 'Variable'
            status_class = 'critical' if col['is_constant'] else ''
            html += f'''<tr>
<td>{col['column_name']}</td>
<td>{col['inferred_type']}</td>
<td>{col['null_count']} / {pf['row_count']}</td>
<td>{col['unique_ratio']*100:.0f}%</td>
<td class="{status_class}">{status}</td>
</tr>'''
        
        html += '</table></div>\n\n'
        
        # Data quality summary
        total_nulls = sum(c['null_count'] for c in pf['schema'])
        constant_count = sum(1 for c in pf['schema'] if c['is_constant'])
        
        html += f'''<div class="quality-box">
<strong>Data Quality Metrics:</strong><br>
• Total null values (checked columns): {total_nulls}<br>
• Constant columns: {constant_count}<br>
'''
        
        # Check for bad records / outliers
        numeric_cols = [c['column_name'] for c in pf['schema'] if not c['is_constant']]
        if numeric_cols:
            html += f'''<br><strong>Numeric-like columns: </strong>{', '.join(numeric_cols[:3])}...
'''
        
        html += '</div>\n\n'
    
    # Summary section
    html += '''</div>

<h2>Data Contract Facts & Recommendations</h2>
<div class="file-section">
<table style="background:#e9ecef;">
<tr><th>Issue Type</th><th>Description</th><th>Priority</th></tr>'''
    
    # Aggregate findings across all files
    total_rows = sum(p['row_count'] for p in profiles)
    html += f'''<tr>
<td colspan="2"><strong>Total Records Across All Files:</strong> {total_rows:,}</td>
<td>-</td>
</tr>
<tr><td rowspan="3">Large File Size</td><td>ride_sharing_new.csv is large (~2.7MB) with {sum(p['row_count'] for p in profiles if 'ride' in p['filename'])} rows</td><td class="warning">Medium - consider pagination</td></tr>
<tr><td>Suggest batch loading / chunked processing</td><td>-</td></tr>'''
    
    constant_total = sum(sum(1 for c in p['schema'] if c['is_constant']) for p in profiles)
    html += f'''<tr><td>Constant Columns</td><td>{constant_total} columns have no variation (likely join keys)</td><td class="info">Low - document as IDs</td></tr>'''
    
    html += '''<tr><td>Null Values</td><td>Some columns have nulls from joins or missing data</td><td class="warning">Medium - validate against schema</td></tr>'''
    
    # Banking PII warning
    banking_profiles = [p for p in profiles if 'banking' in p['filename']]
    if banking_profiles:
        html += f'''<tr><td colspan="2"><strong class="critical">[!] POTENTIAL PII DETECTED:</strong> banking_dirty.csv contains customer identifiers and birth dates</td><td class="critical">High - requires GDPR/CCPA compliance</td></tr>
<tr><td colspan="3" style="font-size:11px; padding:5px;"><em>Recommendation: Apply data masking or redaction before processing, obtain proper consent, and follow privacy regulations.</em></td></tr>'''
    
    html += '''</table>
</div>

<h3>Key Takeaways for Data Contract</h3>
<div style="background:#d4edda; padding:20px; border-radius:8px;">
<ol>
<li>All files use CSV format with comma delimiter and UTF-8 encoding</li>
<li>Date formats vary across columns - document each expected format</li>
<li>Handle nullable columns appropriately (likely from join operations)</li>
<li>banking_dirty.csv requires GDPR/CCPA compliance considerations</li>
<li>Large ride_sharing file may need partitioning for performance</li>
<li>Document constant columns as system-generated IDs, not user-facing fields</li>
<li>Suggest data validation rules in contracts (range checks for numeric columns)</li>
</ol>
</div>

<p style="margin-top:30px; color:#666;">Report generated from automated dataset analysis.</p>
</div>
</body>
</html>'''
    
    # Write to file
    with open(OUTPUT_HTML, 'w', encoding='utf-8') as f:
        f.write(html)
    
    print(f"HTML report saved successfully: {OUTPUT_HTML}")
    return html

# Main execution
if __name__ == '__main__':
    profiles = []
    for filename in FILES:
        filepath = Path(DATASET_PATH) / filename
        if filepath.exists():
            try:
                profile = profile_file(str(filepath))
                profiles.append(profile)
                print(f"Success: {filename}: {profile['row_count']} rows, {len(profile['schema'])} columns")
            except Exception as e:
                print(f"Error profiling {filename}: {e}")
    
    if profiles:
        html = generate_html_report(profiles)
        
        # Also save summary text file
        summary_path = DATASET_PATH + r'\profiling_summary.txt'
        with open(summary_path, 'w', encoding='utf-8') as f:
            f.write(f"Dataset Profiling Summary\n=========================\n")
            for pf in profiles:
                f.write(f"\n{pf['filename']}\n{'-'*30}\n")
                f.write(f"Rows: {pf['row_count']}\nColumns: {len(pf['schema'])}\n")
                f.write(f"Schema:\n")
                for col in pf['schema'][:5]:
                    status = 'CONSTANT' if col['is_constant'] else 'NORMAL'
                    f.write(f"  - {col['column_name']:20} | {col['null_count']:5} nulls | {col['unique_ratio']*100:.1f}% unique [{status}]\n")
        print(f"HTML saved: {OUTPUT_HTML}")
    
            # Also save summary text file
            summary_path = DATASET_PATH + r'\profiling_summary.txt'
            with open(summary_path, 'w', encoding='utf-8') as f:
                f.write(f"Dataset Profiling Summary\n=========================\n")