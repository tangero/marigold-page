---
slug: "t-ads"
url: "/mobilnisite/slovnik/t-ads/"
type: "slovnik"
title: "T-ADS – Terminating Access Domain Selection"
date: 2025-01-01
abbr: "T-ADS"
fullName: "Terminating Access Domain Selection"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/t-ads/"
summary: "Funkce v IMS, která určuje nejvhodnější přístupovou síť (CS nebo PS) pro doručení příchozího hovoru uživateli registrovanému ve více doménách. Umožňuje bezproblémové doručení hovoru a optimalizaci síť"
---

T-ADS je funkce IMS, která vybírá nejvhodnější přístupovou síť (CS nebo PS) pro doručení příchozího hovoru uživateli registrovanému ve více doménách, aby umožnila bezproblémové doručení hovoru a optimalizovala síťové zdroje.

## Popis

Terminating Access Domain Selection (T-ADS) je síťová služební schopnost v architektuře IP Multimedia Subsystem (IMS), definovaná pro zpracování směrování koncových (příchozích) hlasových nebo video relací (např. [SIP](/mobilnisite/slovnik/sip/) INVITEs) pro uživatele, kteří jsou současně registrovaní přes přepojované okruhy ([CS](/mobilnisite/slovnik/cs/)) i přepojované pakety ([PS](/mobilnisite/slovnik/ps/)). Tento scénář je běžný v raných nasazeních IMS a během síťových přechodů, kdy může mít uživatel CS registraci (přes [MSC](/mobilnisite/slovnik/msc/) Server) pro legacy hlas a IMS registraci přes LTE/5G NR pro VoLTE/VoNR. Základní problém, který T-ADS řeší, je rozhodnutí, zda směrovat příchozí hovor do CS domény uživatele (např. jako běžný CS hovor) nebo do jeho PS/IMS domény (jako VoIP hovor).

Architektonicky je logika T-ADS typicky implementována uvnitř Serving-Call Session Control Function ([S-CSCF](/mobilnisite/slovnik/s-cscf/)) nebo může být delegována na Application Server ([AS](/mobilnisite/slovnik/as/)). Když dorazí příchozí požadavek na SIP relaci pro uživatele, S-CSCF spustí proceduru T-ADS. S-CSCF dotazuje Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)), aby získal aktuální registrační stav uživatele napříč doménami, uložený jako součást IMS Subscription Profile uživatele. To zahrnuje CS a IMS registrační stavy uživatele, přidružené kontaktní adresy (např. číslo MSC serveru pro CS, SIP [URI](/mobilnisite/slovnik/uri/) pro IMS) a případné preference nebo schopnosti definované operátorem. Na základě těchto informací, spolu s případnými dalšími kritérii, jako jsou preference volaného, schopnosti volajícího a síťové politiky, funkce T-ADS provede výběr.

Výběrový algoritmus sleduje standardizovaná pravidla a priority. Běžná kritéria zahrnují: preferování PS/IMS domény, pokud je uživatel IMS-registrovaný a podporuje požadovanou službu (např. VoLTE), přechod na CS, pokud je IMS registrace nedostupná nebo nevhodná; zohlednění explicitního identifikátoru komunikační služby uživatele (např. ICSI) nebo implicitních požadavků služby; a aplikaci politik konfigurovaných operátorem pro vyrovnávání zatížení nebo kontinuitu služeb. Jakmile je výběr proveden, S-CSCF směruje relaci odpovídajícím způsobem – buď přepošle SIP požadavek v rámci IMS core, nebo iniciuje přesměrování do CS sítě pomocí mechanismů jako Service Centralization and Continuity (SRVCC) nebo spolupráce s CS sítí. T-ADS je klíčová pro umožnění plynulé kontinuity služeb a efektivního využití síťových zdrojů v konvergovaném prostředí s více přístupy.

## K čemu slouží

T-ADS byla vyvinuta pro řešení výzvy doručování hlasových a multimediálních služeb v konvergovaném síťovém prostředí, kde mohou být uživatelé dosažitelní přes tradiční mobilní sítě s přepojováním okruhů (jako 2G/3G) i přes sítě IMS s přepojováním paketů. Před IMS a T-ADS mohl uživatel s dvojitou registrací (např. UE s GSM i IMS schopnostmi) čelit selháním v doručení hovoru nebo suboptimálnímu směrování, pokud síť nemohla inteligentně vybrat nejlepší doménu. T-ADS to řeší tím, že poskytuje standardizovaný, politikami řízený výběrový mechanismus, který zajišťuje zachování uživatelského zážitku bez ohledu na použitou přístupovou síť. Byla motivována přechodem od čistého CS hlasu k Voice over LTE (VoLTE) a potřebou bezproblémové kontinuity služeb. Bez T-ADS by mohlo být příchozí volání směrováno do nedostupné domény, což by způsobovalo zmeškané hovory nebo špatný uživatelský zážitek. T-ADS umožňuje operátorům optimalizovat síťové zdroje a uživatelský zážitek výběrem nejvhodnější domény na základě registračních a politických dat v reálném čase.

## Klíčové vlastnosti

- Určuje optimální přístupovou doménu (CS nebo PS/IMS) pro doručení koncové relace
- Využívá data o registraci uživatele z HSS a politiky operátora
- Typicky prováděna S-CSCF nebo vyhrazeným Application Server v IMS core
- Podporuje kontinuitu služeb a bezproblémový uživatelský zážitek v sítích s více přístupy
- Integruje se s procedurami jako Single Radio Voice Call Continuity (SRVCC) pro předávání hovorů
- Umožňuje efektivní využití síťových zdrojů a vyrovnávání zatížení

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)

## Definující specifikace

- **TS 23.292** (Rel-19) — IMS Centralized Services (ICS) Architecture
- **TS 24.292** (Rel-19) — IMS Centralized Services (ICS) Protocol
- **TS 29.806** (Rel-12) — P-CSCF Restoration Analysis & Solutions

---

📖 **Anglický originál a plná specifikace:** [T-ADS na 3GPP Explorer](https://3gpp-explorer.com/glossary/t-ads/)
