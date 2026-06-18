---
slug: "s-ran"
url: "/mobilnisite/slovnik/s-ran/"
type: "slovnik"
title: "S-RAN – Shared Radio Access Network"
date: 2025-01-01
abbr: "S-RAN"
fullName: "Shared Radio Access Network"
category: "Radio Access Network"
segment: "Management"
canonical: "https://3gpp-explorer.com/glossary/s-ran/"
summary: "S-RAN (Shared Radio Access Network) je architektonický a operační model, ve kterém je infrastruktura rádiové přístupové sítě (základnové stanice, rádiové jednotky) sdílena mezi více operátory mobilníc"
---

S-RAN je architektonický a operační model, ve kterém je infrastruktura rádiové přístupové sítě sdílena mezi více operátory mobilních sítí za účelem snížení nákladů, rychlejšího nasazení a efektivního využití spektra.

## Popis

Sdílená rádiová přístupová síť (S-RAN) označuje scénář nasazení, ve kterém je infrastruktura rádiové přístupové sítě (RAN) – včetně základnových stanic (gNBs v 5G, eNBs v 4G), antén a někdy i přenosové sítě – využívána více operátory mobilních sítí (MNOs) nebo virtuálními operátory (MVNOs). Jedná se o formu sdílení sítě, která přesahuje sdílení jádrové sítě. V uspořádání S-RAN účastnící se operátoři sdílejí fyzické prvky RAN, zatímco si zachovávají nezávislé jádrové sítě, databáze účastníků a servisní platformy. To umožňuje každému operátorovi poskytovat vlastní služby a udržovat kontrolu nad svými účastníky, přičemž výrazně snižuje kapitálové a provozní výdaje na rádiové vrstvě.

Technická implementace S-RAN může následovat různé modely definované 3GPP, především Multi-Operator Core Network ([MOCN](/mobilnisite/slovnik/mocn/)) a Gateway Core Network ([GWCN](/mobilnisite/slovnik/gwcn/)). V modelu MOCN sdílený uzel RAN vysílá identifikátory veřejné pozemní mobilní sítě ([PLMN](/mobilnisite/slovnik/plmn/)) všech sdílejících operátorů. Uživatelské zařízení (UE) připojené k buňce si může vybrat svou domovskou PLMN a RAN směruje signalizaci a uživatelská data do příslušné jádrové sítě operátora na základě vybrané PLMN. RAN musí podporovat samostatné konfigurační kontexty pro každého operátora, včetně odlišných identit buněk, sledovacích oblastí a potenciálně i politik správy rádiových zdrojů. Model GWCN je varianta, ve které operátoři sdílejí také některé prvky jádrové sítě, jako je Mobility Management Entity ([MME](/mobilnisite/slovnik/mme/)) v 4G.

Klíčovými architektonickými komponentami umožňujícími S-RAN jsou sdílený hardware základnových stanic, sdílené nebo rozdělené rádiové spektrum a přenosová síť spojující RAN s jádrovou sítí každého operátora. RAN musí implementovat robustní izolační mechanismy, aby zajistila, že provoz a signalizace jednoho operátora nebudou interferovat s jiným, a aby zabránila neoprávněnému přístupu mezi operátory. To zahrnuje logické oddělení na datové rovině a pečlivé řízení operačních podpůrných systémů ([OSS](/mobilnisite/slovnik/oss/)). S-RAN je zvláště cenná pro pokrytí nákladných oblastí (např. venkovských), vnitřních prostor (letiště, stadiony) nebo pro nové účastníky trhu, kteří chtějí spustit služby bez neúnosných nákladů na vybudování kompletní RAN infrastruktury od nuly.

## K čemu slouží

S-RAN byla vyvinuta, aby řešila ekonomické a praktické výzvy nasazení hustých rádiových přístupových sítí, zejména když poptávka po mobilních datech prudce rostla a přechod sítí na 4G a později 5G vyžadoval významné investice. Výstavba duplicitní RAN infrastruktury více operátory ve stejné geografické oblasti je často ekonomicky neefektivní, vede k vizuálnímu znečištění a může čelit regulačním překážkám při získávání lokalit. S-RAN poskytuje řešení tím, že umožňuje operátorům sdílet nejnákladnější část sítě – rádiovou infrastrukturu – a tím snižovat kapitálové ([CAPEX](/mobilnisite/slovnik/capex/)) i provozní ([OPEX](/mobilnisite/slovnik/opex/)) výdaje, zatímco mohou stále soutěžit na úrovni služeb a funkcí jádrové sítě.

Koncept získal formální specifikaci v 3GPP přibližně od Release 12, vyvinul se z dřívějších, omezenějších konceptů sdílení. Byl motivován potřebou zlepšit pokrytí, zejména ve venkovských a nedostatečně pokrytých oblastech, kde je obchodní případ pro jediného operátora slabý. Sdílení činí nasazení životaschopným. Dále je pro nasazení 5G, která vyžadují hustší síť buněk, S-RAN považována za klíčový faktor umožňující rychlé a nákladově efektivní rozšíření. Podporuje také model neutrálního hostitele, kdy třetí strana vybuduje a provozuje RAN, která je pronajímána více MNOs, běžně používaný ve velkých vnitřních prostorách nebo privátních sítích. S-RAN tak vyvažuje konkurenci a spolupráci v telekomunikačním průmyslu, podporuje efektivitu infrastruktury bez obětování diferenciace služeb.

## Klíčové vlastnosti

- Sdílená fyzická RAN infrastruktura (základnové stanice, antény) mezi více operátory
- Podpora modelů sdílení definovaných 3GPP: MOCN a GWCN
- Vysílání více PLMN identifikátorů z jedné buňky
- Směrování provozu na základě RAN k příslušné jádrové síti operátora
- Logická izolace zdrojů a politik pro každého operátora
- Umožňuje nákladově efektivní pokrytí ve venkovských oblastech a hustě zastavěných prostorách

## Související pojmy

- [MOCN – Multiple Operator Core Network](/mobilnisite/slovnik/mocn/)
- [PLMN – Public Land Mobile Network](/mobilnisite/slovnik/plmn/)

## Definující specifikace

- **TS 23.725** (Rel-16) — Study on URLLC Architecture Enhancements
- **TS 32.130** (Rel-19) — Network Sharing OAM&P Requirements
- **TS 32.851** (Rel-12) — Network Sharing OAM Requirements
- **TS 33.825** (Rel-16) — Security for 5G URLLC Services

---

📖 **Anglický originál a plná specifikace:** [S-RAN na 3GPP Explorer](https://3gpp-explorer.com/glossary/s-ran/)
