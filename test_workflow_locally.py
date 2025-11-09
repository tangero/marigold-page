#!/usr/bin/env python3
"""
Lokální test simulující GitHub Actions workflow pro commit c599319facf
"""

import subprocess
import sys

def run_git_command(cmd):
    """Run git command and return output."""
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=10)
        return result.stdout.strip()
    except Exception as e:
        print(f"❌ Git command failed: {e}")
        return ""

def main():
    print("🔍 DIAGNOSTIKA: Proč se neposlala notifikace pro Zohran Mamdani článek?")
    print("=" * 80)

    # Simulovat checkout s fetch-depth=2 není možné lokálně,
    # ale můžeme otestovat, co by viděl skript

    print("\n1️⃣  Kontrola commitu c599319facf (Create article)")
    print("-" * 80)

    article_path = "_posts/2025/2025-11-05-zohran-mamdani-starosta-new-york.md"

    # Test 1: Existuje soubor?
    import os
    if os.path.exists(article_path):
        print(f"✅ Soubor existuje: {article_path}")
    else:
        print(f"❌ Soubor NEexistuje: {article_path}")
        return

    # Test 2: Kolik commitů má soubor?
    output = run_git_command(f'git log --oneline --follow "{article_path}" | wc -l')
    count = int(output.strip()) if output.strip().isdigit() else 0
    print(f"\n2️⃣  Počet commitů pro soubor: {count}")
    print("-" * 80)

    if count <= 1:
        print("✅ is_new_article() by vrátil TRUE → notifikace by se MĚLA poslat")
    else:
        print("❌ is_new_article() by vrátil FALSE → notifikace by se NEPOSLALA")
        print(f"\n⚠️  PROBLÉM: Soubor má {count} commity, ale očekáváme ≤ 1 pro nový článek!")

    # Test 3: Jaké commity soubor má?
    print(f"\n3️⃣  Historie commitů pro soubor:")
    print("-" * 80)
    commits = run_git_command(f'git log --oneline --follow "{article_path}"')
    for line in commits.split('\n'):
        print(f"   {line}")

    # Test 4: Byl článek přidán v commitu c599319facf?
    print(f"\n4️⃣  Kontrola commitu c599319facf:")
    print("-" * 80)
    commit_files = run_git_command("git show --name-only --format= c599319facf")
    if article_path in commit_files:
        print(f"✅ Článek byl přidán v commitu c599319facf")
    else:
        print(f"❌ Článek NEBYL v commitu c599319facf")
        print(f"\nSoubory v commitu:")
        for f in commit_files.split('\n'):
            if f.strip():
                print(f"   {f}")

    # Test 5: Co by viděl get_changed_files() při commitu c599319facf?
    print(f"\n5️⃣  Simulace get_changed_files() pro commit c599319facf:")
    print("-" * 80)
    # Simulovat checkout na c599319facf a diff s předchozím
    changed = run_git_command("git diff --name-only c599319facf~1 c599319facf")
    if article_path in changed:
        print(f"✅ get_changed_files() by detekoval: {article_path}")
    else:
        print(f"❌ get_changed_files() by NEDETEKOVAL článek!")
        print(f"\nZměněné soubory:")
        for f in changed.split('\n'):
            if f.strip():
                print(f"   {f}")

    # Test 6: Workflow path filter
    print(f"\n6️⃣  GitHub Actions path filter test:")
    print("-" * 80)
    patterns = ["_posts/**/*.md", "_vibecoding/**/*.md"]
    import fnmatch

    for pattern in patterns:
        # Jednoduchý test - nahradit ** za *
        simple_pattern = pattern.replace("**", "*")
        if fnmatch.fnmatch(article_path, simple_pattern):
            print(f"✅ Path '{article_path}' matchuje pattern '{pattern}'")
        else:
            print(f"❌ Path '{article_path}' NEmatchuje pattern '{pattern}'")

    # Test 7: Časová linie
    print(f"\n7️⃣  Časová linie relevantních commitů:")
    print("-" * 80)
    timeline = run_git_command(
        "git log --oneline --date=iso-strict --format='%h %ad %s' | "
        "grep -E '(4bc0252|c599319|e2c3d27)'"
    )
    for line in timeline.split('\n'):
        if line.strip():
            print(f"   {line}")

    # Závěr
    print("\n" + "=" * 80)
    print("📊 ZÁVĚR:")
    print("=" * 80)

    if count <= 1:
        print("\n✅ Skript by měl poslat notifikaci (is_new_article() = TRUE)")
        print("\n❓ Možné příčiny, proč se notifikace NEPOSLALA:")
        print("   1. GitHub Actions workflow se NESPUSTIL")
        print("      → Zkontrolujte GitHub Actions logs v UI")
        print("      → URL: https://github.com/tangero/marigold-page/actions")
        print("\n   2. GitHub Secrets nejsou nastavené")
        print("      → ONESIGNAL_REST_API_KEY")
        print("      → ONESIGNAL_APP_ID")
        print("\n   3. Workflow se spustil, ale SELHAL")
        print("      → Zkontrolujte logs v GitHub Actions")
        print("\n   4. fetch-depth: 2 způsobil problém")
        print("      → is_new_article() nevrátil správný výsledek")
    else:
        print(f"\n❌ Skript by NEPOSLAL notifikaci (is_new_article() = FALSE)")
        print(f"\n   Důvod: Soubor má {count} commity, ale očekáváme ≤ 1")
        print(f"\n   První commit: {commits.split(chr(10))[-1] if commits else 'N/A'}")
        print(f"   Druhý commit: {commits.split(chr(10))[0] if len(commits.split(chr(10))) > 1 else 'N/A'}")

    print("\n" + "=" * 80)

if __name__ == "__main__":
    main()
