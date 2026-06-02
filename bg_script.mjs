import fs from 'fs';
import path from 'path';

const dir = process.cwd();
const files = [
  'schools.html',
  'mission.html',
  'achievements.html',
  'branches.html',
  'contact.html',
  'register.html'
];

for (const file of files) {
  let filepath = path.join(dir, file);
  if (!fs.existsSync(filepath)) continue;
  
  let content = fs.readFileSync(filepath, 'utf-8');
  
  // Section background
  content = content.replace(
    /background: linear-gradient\(135deg, #f8f9fc 0%, #ffffff 100%\);/g,
    'background: linear-gradient(135deg, var(--burgundy) 0%, #681120 100%);'
  );
  content = content.replace(
    /radial-gradient\(rgba\(139,26,43,0.03\) 1.5px/g,
    'radial-gradient(rgba(255,255,255,0.08) 1.5px'
  );
  content = content.replace(
    /radial-gradient\(circle, rgba\(139,26,43,0.04\) 0%/g,
    'radial-gradient(circle, rgba(255,255,255,0.06) 0%'
  );
  content = content.replace(
    /radial-gradient\(circle, rgba\(76, 96, 171,0.03\) 0%/g,
    'radial-gradient(circle, rgba(0,0,0,0.2) 0%'
  );
  content = content.replace(
    /stroke=%22rgba\(139,26,43,0.05\)%22/g,
    'stroke=%22rgba(255,255,255,0.05)%22'
  );
  
  // Eyebrow and Headings
  content = content.replace(
    /color: var\(--navy\); opacity: 0.5;/g,
    'color: rgba(255,255,255,0.7); opacity: 1;'
  );
  content = content.replace(
    /color: var\(--navy\); margin-bottom: 40px/g,
    'color: var(--white); margin-bottom: 40px'
  );
  content = content.replace(
    /color: var\(--navy\); z-index: 1/g,
    'color: var(--white); z-index: 1'
  );
  content = content.replace(
    /background: var\(--burgundy\); z-index: -1; opacity: 0.15;/g,
    'background: var(--navy); z-index: -1; opacity: 0.3;'
  );
  content = content.replace(
    /background: linear-gradient\(90deg, transparent, var\(--burgundy\), transparent\);/g,
    'background: linear-gradient(90deg, transparent, rgba(255,255,255,0.3), transparent);'
  );
  
  // Paragraph Colors
  content = content.replace(
    /color: var\(--navy\); line-height: 1.6; font-weight: 500; opacity: 0.8;/g,
    'color: rgba(255,255,255,0.9); line-height: 1.6; font-weight: 400; opacity: 1;'
  );
  content = content.replace(
    /color: var\(--burgundy\); font-weight: 800;/g,
    'color: var(--white); font-weight: 800;'
  );
  content = content.replace(
    /color: rgba\(255,255,255,1\); max-width: 750px; margin: 0 auto; font-size: 1.6rem; line-height: 1.5; font-weight: 500;/g, // Achievements specific
    'color: rgba(255,255,255,0.9); max-width: 850px; margin: 0 auto; font-size: 1.6rem; line-height: 1.6; font-weight: 400;'
  );

  fs.writeFileSync(filepath, content);
}

console.log("Updated Backgrounds!");
