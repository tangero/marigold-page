---
slug: "bcs"
url: "/mobilnisite/slovnik/bcs/"
type: "slovnik"
title: "BCS – Binary Coded Signalling"
date: 2025-01-01
abbr: "BCS"
fullName: "Binary Coded Signalling"
category: "Services"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/bcs/"
summary: "BCS je fáze přenosu faksimile (faxu) definovaná doporučením ITU-T T.30, která umožňuje digitální signalizaci pro řízení hovoru a vyjednávání schopností. V 3GPP je adaptována pro okruhově spínané faxov"
---

BCS je digitální signalizační procedura adaptovaná 3GPP pro okruhově spínané faxové služby v mobilních sítích, která řídí navázání, vyjednávání a ukončení faxového hovoru za účelem zajištění spolehlivé komunikace.

## Popis

Binary Coded Signalling (BCS) je klíčová protokolová fáze v rámci standardu [ITU-T](/mobilnisite/slovnik/itu-t/) T.30 pro faksimilní komunikaci, speciálně navržená pro digitální signalizaci. V kontextu sítí 3GPP je BCS využívána pro podporu okruhově spínaných faxových služeb, jako je fax skupiny 3, v mobilních systémech. Fáze BCS nastává po počátečním handshake a před vlastním přenosem obrazových dat (fází zprávy). Používá rámcovou strukturu vysokorychlostního spojového řízení ([HDLC](/mobilnisite/slovnik/hdlc/)) pro výměnu binárně kódovaných řídicích zpráv mezi vysílajícím a přijímajícím faxovým terminálem. Tyto zprávy vyjednávají přenosové parametry, potvrzují schopnosti a řídí proceduru hovoru, čímž zajišťují, že se oba terminály shodnou na modulačních schématech, přenosových rychlostech a režimech opravy chyb před pokračováním.

Z architektonického hlediska BCS funguje v uživatelské rovině okruhově spínané domény v sítích 3GPP. Je implementována v koncovém zařízení (např. faxový přístroj nebo faxový modem) a podporována síťovými elementy, jako je Mobile Switching Centre ([MSC](/mobilnisite/slovnik/msc/)), pro směrování hovorů a správu přenosu. Zprávy BCS jsou přenášeny přes transparentní nebo netransparentní datovou přenosovou službu, typicky pomocí asynchronního okruhově spínaného datového hovoru. Mezi klíčové komponenty patří HDLC flag sekvence pro ohraničení rámců, adresní a řídicí pole pro správu spoje a kontrolní sekvence rámce ([FCS](/mobilnisite/slovnik/fcs/)) pro detekci chyb. Informační pole obsahuje vlastní binární příkazy a odpovědi T.30, jako je Digital Identification Signal (DIS), Digital Command Signal ([DCS](/mobilnisite/slovnik/dcs/)) a Confirmation to Receive ([CFR](/mobilnisite/slovnik/cfr/)).

Během provozu BCS umožňuje strukturované vyjednávání: volaný terminál odešle zprávu DIS udávající jeho schopnosti (např. podporované datové rychlosti, rozlišení). Volající terminál odpoví zprávou DCS pro výběr parametrů, následovanou tréninkovou sekvencí pro optimalizaci fyzického spoje. Po úspěšném tréninku zpráva CFR potvrdí připravenost a dojde k přechodu do fáze zprávy pro přenos faxové stránky. BCS také zvládá řízení během hovoru, například příkazy po stránce pro více-stránkové dokumenty. Její role v 3GPP spočívá v zajištění interoperability mezi mobilními faxovými službami a tradičními faxovými systémy [PSTN](/mobilnisite/slovnik/pstn/)/[ISDN](/mobilnisite/slovnik/isdn/), přičemž udržuje spolehlivost prostřednictvím standardizovaného zpracování chyb a procedur opakovaného přenosu pro poškozené rámce.

Integrace BCS do specifikací 3GPP, jako jsou TS 23.046 a TS 43.045, definuje adaptace pro interakce s rádiovým přístupem a jádrem sítě. To zahrnuje mapování na protokoly rádiového rozhraní a spolupráci s PSTN pro faxové hovory end-to-end. BCS je nezbytná pro podporu legacy faxu v sítích 2G (GSM), 3G (UMTS) a raných 4G (LTE), kde převažují okruhově spínané služby, ačkoli její význam poklesl s úpadkem faxu a přechodem na plně IP sítě.

## K čemu slouží

BCS byla vytvořena k řešení omezení dřívějších analogových signalizačních metod ve faksimilním přenosu, jako jsou před-zprávové procedury T.30 používající tónové signály (např. CNG, CED). Tyto analogové metody byly náchylné k chybám v hlučném prostředí a nabízely omezenou flexibilitu pro vyjednávání složitých schopností. BCS zavedla digitální, binárně kódovanou signalizační fázi pro zvýšení spolehlivosti, rychlosti a funkčnosti. Použitím HDLC rámcování a detekce chyb BCS snižuje riziko nesprávné interpretace a umožňuje sofistikovanější vyjednávání parametrů, podporuje vyšší datové rychlosti a pokročilé funkce jako režim opravy chyb (ECM). To bylo klíčové pro zlepšení kvality a efektivity faxu přes PSTN i mobilní sítě.

V 3GPP byl účel začlenění BCS, počínaje Release 99, zajistit bezproblémovou podporu okruhově spínaných faxových služeb v mobilní telekomunikaci. Jak se sítě GSM a UMTS vyvíjely, byla potřeba zachovat kompatibilitu s existující faxovou infrastrukturou a zároveň využít digitální mobilní technologie. BCS umožňuje mobilním terminálům fungovat jako faxové koncové body a vyjednávat schopnosti se vzdálenými faxovými přístroji přes síť. Řeší problémy jako interoperabilita mezi mobilními a pevnými faxovými zařízeními, řízení navázání hovoru v rádiovém prostředí s potenciální latencí a chybami a poskytnutí standardizované metody pro fax přes okruhově spínané datové přenosy. To bylo motivováno rozšířeným používáním faxu pro obchodní a právní dokumenty, které vyžadovaly spolehlivá mobilní faxová řešení před nástupem rozšířených internetových alternativ.

Historicky BCS řešila přechod od analogového k digitálnímu faxu, umožňujíc funkce jako superjemné rozlišení a rychlejší modulace. V 3GPP podporovala služby jako faxová pošta a store-and-forward fax, jak je definováno ve specifikacích. Nicméně s vyřazováním okruhově spínaných domén ve prospěch VoLTE a IP Multimedia Subsystem (IMS) význam BCS poklesl, ačkoli zůstává součástí podpory legacy ve specifikacích až do nedávných release.

## Klíčové vlastnosti

- Digitální signalizace využívající HDLC rámce pro spolehlivé řízení faxového hovoru
- Výměna binárně kódovaných zpráv pro vyjednávání schopností (např. DIS, DCS, CFR)
- Detekce chyb pomocí kontrolní sekvence rámce (FCS) pro zajištění integrity dat
- Podpora pokročilých faxových funkcí jako Error Correction Mode (ECM) a vysokorychlostní modulace
- Interoperabilita se standardem ITU-T T.30 pro end-to-end faxovou komunikaci přes sítě
- Adaptace pro okruhově spínané přenosové služby v mobilních systémech 3GPP

## Související pojmy

- [HDLC – High Level Data Link Control](/mobilnisite/slovnik/hdlc/)

## Definující specifikace

- **TS 23.046** (Rel-4) — GSM Facsimile Group 3 Service Procedures
- **TS 23.146** (Rel-19) — 3G Facsimile Group 3 Technical Realization
- **TS 36.714** — 3GPP TR 36.714
- **TS 36.715** — 3GPP TR 36.715
- **TS 36.716** — 3GPP TR 36.716
- **TS 36.853** — 3GPP TR 36.853
- **TS 37.716** — 3GPP TR 37.716
- **TS 37.717** — 3GPP TR 37.717
- **TS 37.718** — 3GPP TR 37.718
- **TS 37.719** (Rel-19) — 3GPP TR 37.719: Dual Connectivity Band Combinations
- **TS 37.872** (Rel-15) — Technical Report on SUL & LTE-NR DC with SUL
- **TS 37.898** (Rel-19) — Rel-19 HPUE for EN-DC Band Combinations
- **TS 38.101** (Rel-19) — NR User Equipment Radio Transmissions
- **TS 38.521** (Rel-19) — NR Physical Layer UE Conformance Testing
- **TS 38.716** — 3GPP TR 38.716
- … a dalších 16 specifikací

---

📖 **Anglický originál a plná specifikace:** [BCS na 3GPP Explorer](https://3gpp-explorer.com/glossary/bcs/)
