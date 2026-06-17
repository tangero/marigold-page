---
slug: "lals"
url: "/mobilnisite/slovnik/lals/"
type: "slovnik"
title: "LALS – Lawful Access Location Services"
date: 2025-01-01
abbr: "LALS"
fullName: "Lawful Access Location Services"
category: "Security"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/lals/"
summary: "Soubor standardizovaných schopností podle 3GPP, který umožňuje orgánům činným v trestním řízení vyžádat a přijímat informace o poloze uživatelského zařízení (UE) cílového účastníka pro účely zákonného"
---

LALS je soubor standardizovaných schopností podle 3GPP, který umožňuje orgánům činným v trestním řízení vyžádat a přijímat informace o poloze cílového účastníka pro účely zákonného odposlechu.

## Popis

Lawful Access Location Services (LALS) je standardizovaný rámec v rámci 3GPP, který rozšiřuje schopnosti zákonného odposlechu ([LI](/mobilnisite/slovnik/li/)) o poskytování informací o poloze cílového účastníka v reálném čase nebo historických. Funguje jako specializovaná služba v rámci širší architektury LI a komunikuje s síťovými elementy schopnými určit polohu UE, jako je Gateway Mobile Location Centre ([GMLC](/mobilnisite/slovnik/gmlc/)), Serving Mobile Location Centre (SMLC) nebo Location Management Function ([LMF](/mobilnisite/slovnik/lmf/)). Systém je aktivován na základě zákonného pověření od orgánu činného v trestním řízení ([LEA](/mobilnisite/slovnik/lea/)), které je zprostředkováno prostřednictvím zařízení pro monitorování pro orgány činné v trestním řízení ([LEMF](/mobilnisite/slovnik/lemf/)). Administrativní funkce ([ADMF](/mobilnisite/slovnik/admf/)) a doručovací funkce (DFs) sítě 3GPP přijmou autorizovaný požadavek na odposlech a koordinují s příslušnými uzly lokalizační služby sběr požadovaných lokalizačních dat.

Technický provoz zahrnuje několik klíčových rozhraní definovaných ve specifikacích řady 33.1xx. ADMF přijme příkaz k zákonnému odposlechu a distribuuje příslušné identity (např. [IMSI](/mobilnisite/slovnik/imsi/), [MSISDN](/mobilnisite/slovnik/msisdn/)) a parametry lokalizační služby příslušné síťové doručovací funkci. Pro lokalizační služby je to typicky doručovací funkce pro informace o poloze (DF-L). DF-L následně komunikuje prostřednictvím standardizovaných referenčních bodů (např. X1_1, X2) s infrastrukturou lokalizační služby jádra sítě. Touto infrastrukturou může být GMLC v sítích 4G/5G nebo SMLC v kontextech 2G/3G. Požadavek na polohu je zpracován a výsledné zeměpisné souřadnice (např. zeměpisná šířka, délka, nejistota) a časové razítko jsou doručeny zpět přes DF-L do LEMF.

Bezpečnost a integrita jsou u LALS prvořadé. Veškerá komunikace mezi infrastrukturou LI síťového operátora (ADMF, DF) a LEMF orgánu LEA je vysoce zabezpečena, často pomocí vyhrazených, izolovaných sítí nebo silného šifrování přes IPsec tunely. Systém zajišťuje, že jsou provedeny pouze řádně autorizované požadavky a že všechny aktivity jsou zaznamenávány pro účely auditu. LALS podporuje různé metody určení polohy, včetně síťových (např. Cell-ID, časový předstih, OTDOA), založených na UE (např. A-GNSS) nebo hybridních technik, přičemž konkrétní metoda je často dána schopnostmi sítě a přesností požadovanou v příkazu k odposlechu. Její role je klíčová při vyvažování operačních potřeb orgánů činných v trestním řízení s přísnými rámci ochrany soukromí a právní shody, které regulují telekomunikace.

## K čemu slouží

LALS byl vytvořen, aby vyřešil konkrétní mezeru v dřívějších standardech pro zákonný odposlech, které se primárně zaměřovaly na zachycení obsahu komunikace (CC) a informací souvisejících s odposlechem (IRI), jako jsou záznamy hovorů, ale formálně nestandardizovaly poskytování lokalizačních dat. Jak se mobilní zařízení stala všudypřítomnými, poloha účastníka se stala klíčovou informací pro vyšetřování orgánů činných v trestním řízení a národní bezpečnosti. Nedostatek standardizované metody vedl k proprietárním, na operátora specifickým implementacím, které byly pro LEA působící napříč více sítěmi a jurisdikcemi neefektivní.

Zavedení LALS ve verzi 3GPP Release 13 poskytlo jednotný, bezpečný a spolehlivý technický standard pro zákonný odposlech lokalizačních informací. Vyřešil problém interoperability mezi zařízeními různých síťových dodavatelů a různorodými systémy používanými orgány činnými v trestním řízení po celém světě. Definováním jasných architektonických rolí, rozhraní a datových formátů zajistilo, že lokalizační data mohou být vyžádána a doručena konzistentním, ověřitelným a právně přípustným způsobem. Tato standardizace byla motivována vývojem právních požadavků po celém světě, které ukládaly telekomunikačním poskytovatelům povinnost pomáhat při zákonných vyšetřováních, včetně poskytování schopností sledování v reálném čase pod řádným soudním dohledem.

Dále LALS řeší technické a bezpečnostní výzvy integrace citlivých lokalizačních služeb do rámce LI. Zajišťuje, že požadavky na polohu jsou řádně ověřeny a autorizovány, že doručování dat je bezpečné a spolehlivé a že všechny akce jsou auditovatelné, aby se zabránilo zneužití. To chrání jak soukromí jednotlivců, tak integritu právního procesu, a poskytuje nezbytný nástroj pro moderní trestní vyšetřování při současném zachování základních práv.

## Klíčové vlastnosti

- Standardizovaná rozhraní (např. HI2, X1_1, X2) pro vyžádání a doručení lokalizačních dat
- Podpora sledování polohy v reálném čase i poskytování historických záznamů o poloze
- Integrace s lokalizačními službami jádra sítě (GMLC, SMLC, LMF)
- Silné bezpečnostní mechanismy pro autentizaci, autorizaci a zabezpečený přenos dat
- Komplexní auditování a zaznamenávání všech aktivit souvisejících s odposlechem
- Podpora více technologií pro určení polohy (Cell-ID, A-GNSS, OTDOA)

## Definující specifikace

- **TS 33.106** (Rel-19) — Lawful Interception Requirements (Pre-Rel-15)
- **TS 33.107** (Rel-19) — Lawful Interception Architecture & Functions
- **TS 33.108** (Rel-19) — LI Handover Interface Specification
- **TS 33.126** (Rel-19) — Lawful Interception Requirements
- **TS 33.127** (Rel-19) — Lawful Interception Architecture and Functions
- **TS 33.128** (Rel-19) — 3GPP TS 33.128: Lawful Interception Protocols

---

📖 **Anglický originál a plná specifikace:** [LALS na 3GPP Explorer](https://3gpp-explorer.com/glossary/lals/)
