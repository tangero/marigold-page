---
slug: "udvm"
url: "/mobilnisite/slovnik/udvm/"
type: "slovnik"
title: "UDVM – Universal Decompressor Virtual Machine"
date: 2025-01-01
abbr: "UDVM"
fullName: "Universal Decompressor Virtual Machine"
category: "Protocol"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/udvm/"
summary: "Virtuální stroj definovaný protokolem SigComp pro provádění dekompresních algoritmů na komprimovaných signalizačních zprávách. Poskytuje standardizované, bezpečné prostředí pro spouštění bajtkódových"
---

UDVM je virtuální stroj definovaný protokolem SigComp, který provádí dekompresní algoritmy za účelem efektivní dekomprese textových signalizačních zpráv v omezených bezdrátových sítích.

## Popis

Univerzální virtuální stroj pro dekompresi (UDVM) je klíčovou součástí architektury Signalizační komprese (SigComp), standardizované [IETF](/mobilnisite/slovnik/ietf/) a přijaté v rámci 3GPP pro kompresi signalizačních zpráv v IP-based multimediálních subsystémech. SigComp je navržen ke zmenšení velikosti zpráv textových protokolů (jako jsou [SIP](/mobilnisite/slovnik/sip/), [SDP](/mobilnisite/slovnik/sdp/) a [HTTP](/mobilnisite/slovnik/http/)) přenášených přes spoje s omezenou šířkou pásma, zejména v bezdrátových přístupových sítích. UDVM je virtuální stroj – zjednodušené, izolované (sandbox) výkonové prostředí – který spouští programy v bajtkódu speciálně vytvořené pro dekompresi zpráv. Když odesílatel chce poslat komprimovanou zprávu, použije kompresní algoritmus ke generování jak komprimovaných dat, tak odpovídajícího programu dekompresoru (v bajtkódu UDVM). Tento bajtkód je buď odeslán spolu s komprimovanými daty, nebo je na něj odkazováno pomocí standardizovaného identifikátoru, pokud se předpokládá, že jej má příjemce předinstalovaný. Po přijetí načte SigComp modul přijímající entity bajtkód do svého UDVM, spustí jej s komprimovanými daty jako vstupem a UDVM vydá původní, dekomprimovanou zprávu.

Architektura UDVM je navržena pro bezpečnost, determinismus a nízkou paměťovou náročnost, aby spolehlivě fungovala v síťových prvcích, jako je uživatelské zařízení (UE) a servery. Obsahuje paměťovou oblast pro ukládání bajtkódu, komprimované zprávy a pracovního prostoru pro dekompresi spolu se souborem instrukcí, které tuto paměť manipulují za účelem provádění dekompresních operací. Mezi klíčové instrukce patří kopírování bajtů, aritmetické operace a větvení, což umožňuje implementaci různých dekompresních algoritmů, jako jsou DEFLATE, LZSS nebo Huffmanovo kódování. UDVM je „univerzální“, protože není vázán na jediný kompresní algoritmus; místo toho může spustit jakýkoli dobře formovaný program v bajtkódu, který dodržuje jeho instrukční sadu, čímž poskytuje flexibilitu pro přijímání nových kompresních technik bez změny podkladového hardwaru nebo implementace SigComp. Virtuální stroj zahrnuje ochranné mechanismy, jako jsou čítače cyklů a kontrola hranic paměti, aby zabránil zlomyslnému nebo chybnému bajtkódu způsobit nekonečné smyčky nebo přetečení bufferu, čímž zajišťuje síťovou bezpečnost a stabilitu.

V kontextu sítě 3GPP UDVM funguje v rámci vrstvy SigComp, která se nachází mezi aplikační vrstvou (např. SIP) a transportní vrstvou (např. [UDP](/mobilnisite/slovnik/udp/)). Pro služby IMS, když UE odešle zprávu SIP REGISTER nebo INVITE přes úzkopásmový rádiový spoj, může komprese SigComp výrazně zmenšit velikost zprávy, čímž sníží přenosové zpoždění a šetří životnost baterie. UDVM na přijímací straně (např. [P-CSCF](/mobilnisite/slovnik/p-cscf/)) spustí dekompresor, aby rekonstruoval původní SIP zprávu. Role UDVM tedy spočívá v poskytnutí standardizovaného, interoperabilního výkonového engine pro dekompresi, což umožňuje efektivní signalizační kompresi napříč různými implementacemi a síťovými uzly. Jeho návrh zajišťuje, že jsou dosaženy kompresní zisky bez kompromisů v spolehlivosti nebo bezpečnosti signalizačního protokolu.

## K čemu slouží

UDVM byl vytvořen k řešení problému neefektivního využití šířky pásma pro textové signalizační protokoly v omezených síťových prostředích, zejména v časných sítích 3G a novějších mobilních sítích. Protokoly jako [SIP](/mobilnisite/slovnik/sip/) a [HTTP](/mobilnisite/slovnik/http/) používané pro služby IMS jsou verbose a repetitivní, což vede k velkým velikostem zpráv, které spotřebovávají významné rádiové zdroje a prodlužují dobu navázání hovoru. Zatímco kompresní algoritmy existovaly, neexistovala standardizovaná metoda pro dynamické vyjednávání a aplikaci komprese mezi koncovými body, které mohly podporovat různé algoritmy. Architektura SigComp s UDVM jako svým jádrem byla vyvinuta, aby poskytla flexibilní, na algoritmu nezávislé kompresní řešení. Umožňuje koncovým bodům dohodnout se na kompresních technikách výměnou bajtkódu dekompresoru, což umožňuje neustálé zlepšování a přizpůsobování komprese bez nutnosti předstandardizace každého algoritmu.

Motivace pro přístup založený na virtuálním stroji, spíše než pevné zakódování několika dekompresních algoritmů, bylo dosažení univerzálnosti a budoucí odolnosti. Různé síťové podmínky nebo typy zpráv mohou těžit z různých kompresních strategií; pevná sada algoritmů by omezovala optimalizaci. Použitím virtuálního stroje lze nové dekompresory nasadit pouhým přenosem nového bajtkódu, což umožňuje operátorům nebo výrobcům implementovat proprietární nebo optimalizované kompresní schémata při zachování interoperability – pokud oba konce dokážou spustit UDVM. Tím se řešilo omezení předchozích ad-hoc kompresních metod, které buď neexistovaly, nebo vyžadovaly bilaterální dohodu na specifických kodecích, což bránilo jejich širokému přijetí.

Historicky byl UDVM zaveden v 3GPP Rel-6 jako součást standardizace IMS, kde byla efektivní signalizace SIP přes paketově orientované domény UMTS klíčová pro výkon. Jeho vytvoření bylo hnací silou potřeby učinit služby IMS životaschopnými přes rádiové spoje s omezenou šířkou pásma, snížit latenci a zlepšit uživatelský zážitek u VoIP a multimediálních relací. UDVM umožnil, aby se SigComp stal klíčovým enablerem pro nasazení IMS, a zajistil, že signalizační režie neznevýhodní výhody IP multimediálních služeb. Poskytnutím bezpečného, standardizovaného výkonového prostředí také zmírnil bezpečnostní rizika spojená se spouštěním nedůvěryhodného kódu v síťových prvcích, čímž vyvážil flexibilitu s robustností.

## Klíčové vlastnosti

- Virtuální stroj pro provádění programů dekompresního bajtkódu
- Poskytuje bezpečné izolované prostředí (sandbox) s omezeními paměti a cyklů
- Instrukční sada podporující různé dekompresní algoritmy
- Umožňuje signalizační kompresi nezávislou na algoritmu
- Integrální součást architektury IETF SigComp přijaté 3GPP
- Snižuje velikost zpráv SIP/HTTP pro efektivní bezdrátový přenos

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [SIP – Session Initiation Protocol](/mobilnisite/slovnik/sip/)

## Definující specifikace

- **TS 24.229** (Rel-19) — IMS call control protocol based on SIP and SDP

---

📖 **Anglický originál a plná specifikace:** [UDVM na 3GPP Explorer](https://3gpp-explorer.com/glossary/udvm/)
