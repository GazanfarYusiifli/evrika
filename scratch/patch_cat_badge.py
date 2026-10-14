with open('/Users/gazanfaryusifli/Downloads/EvrikaProje/admin.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if "const isLead = m.category === 'leadership';" in line:
        print(f"Found at line {i+1}")
        # Show lines around it
        for j in range(max(0, i-2), min(len(lines), i+6)):
            print(f"{j+1}: {repr(lines[j])}")
        
        replacement = [
            "                  const cat = (m.category || '').toLowerCase();\n",
            "                  const roleLower = (m.role || '').toLowerCase();\n",
            "                  const nameLower = (m.name || '').toLowerCase();\n",
            "                  const isFounder = cat === 'founder' || nameLower.includes('xudaqulu') || roleLower.includes('təsisçi');\n",
            "                  const isDirector = !isFounder && (cat === 'director' || cat === 'leadership' || roleLower.includes('direktor')) && !roleLower.includes('müavini') && !roleLower.includes('maliyyə');\n",
            "                  let catBadge = `<span style=\"background:rgba(59,130,246,0.15); color:#60a5fa; border:1px solid rgba(59,130,246,0.3); padding:3px 10px; border-radius:12px; font-size:0.75rem; font-weight:700;\">İdarə Heyəti</span>`;\n",
            "                  if (isFounder) {\n",
            "                    catBadge = `<span style=\"background:rgba(217,119,6,0.2); color:#fbbf24; border:1px solid rgba(217,119,6,0.4); padding:3px 10px; border-radius:12px; font-size:0.75rem; font-weight:700;\">Təsisçi</span>`;\n",
            "                  } else if (isDirector) {\n",
            "                    catBadge = `<span style=\"background:rgba(139,26,43,0.2); color:#ff6b81; border:1px solid rgba(139,26,43,0.4); padding:3px 10px; border-radius:12px; font-size:0.75rem; font-weight:700;\">Direktor</span>`;\n",
            "                  }\n"
        ]
        # Replace lines i to i+3
        lines[i:i+4] = replacement
        with open('/Users/gazanfaryusifli/Downloads/EvrikaProje/admin.html', 'w', encoding='utf-8') as f_out:
            f_out.writelines(lines)
        print("Updated successfully!")
        break
