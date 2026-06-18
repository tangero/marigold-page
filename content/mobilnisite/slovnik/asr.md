---
slug: "asr"
url: "/mobilnisite/slovnik/asr/"
type: "slovnik"
title: "ASR – Automatic Speech Recognition"
date: 2026-01-01
abbr: "ASR"
fullName: "Automatic Speech Recognition"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/asr/"
summary: "Automatické rozpoznávání řeči (ASR) je síťová služba, která převádí mluvenou řeč na text. Umožňuje hlasem ovládané služby, automatizované zpracování hovorů a funkce usnadnění přístupu v sítích 3GPP. T"
---

ASR je síťová služba, která převádí mluvenou řeč na text, aby umožnila hlasem ovládané služby, automatizované zpracování hovorů a funkce usnadnění přístupu v sítích 3GPP.

## Popis

Automatické rozpoznávání řeči (ASR) v rámci specifikací 3GPP je síťová služba, která přepisuje lidskou řeč do strojově čitelného textu. Funguje jako funkční komponenta, která je typicky hostována v aplikační vrstvě nebo jako součást funkce Media Resource Function ([MRF](/mobilnisite/slovnik/mrf/)) v IP Multimedia Subsystem (IMS). Základní proces zahrnuje zachycení audio signálů z uživatelského zařízení, předzpracování tohoto signálu (např. redukce šumu, detekce koncových bodů), extrakci akustických rysů a aplikaci statistických modelů (jako jsou skryté Markovovy modely nebo, v pozdějších releasech, hluboké neuronové sítě) pro mapování těchto rysů na fonémy, slova a nakonec textový přepis. Služba komunikuje s dalšími síťovými prvky, jako je Telephony Application Server ([TAS](/mobilnisite/slovnik/tas/)) nebo Service Capability Exposure Function ([SCEF](/mobilnisite/slovnik/scef/)/SCEF+/[NEF](/mobilnisite/slovnik/nef/)), aby spouštěla akce na základě rozpoznané řeči, což umožňuje komplexní hlasem řízené služby.

Z architektonického hlediska lze ASR nasadit jako centralizovaný zdroj v jádru sítě nebo, s vývojem směrem k edge computingu, na distribuovaných místech, jako jsou uzly Multi-access Edge Computing ([MEC](/mobilnisite/slovnik/mec/)), pro snížení latence. Klíčové komponenty zahrnují engine pro rozpoznávání řeči, jazykové a akustické modely, definici gramatiky nebo slovní zásoby pro omezení rozpoznávání na specifické domény (zásadní pro aplikace typu příkaz-řízení) a rozhraní pro doručování výsledků rozpoznávání. V IMS call flow je audio z User Equipment (UE) směrováno přes Media Gateway Control Function ([MGCF](/mobilnisite/slovnik/mgcf/)) a Media Gateway ([MGW](/mobilnisite/slovnik/mgw/)) nebo přímo přes Packet Data Network Gateway ([PGW](/mobilnisite/slovnik/pgw/)) do MRF, která hostuje zdroj ASR. MRF následně audio zpracuje a vrátí text nebo indikátor akce aplikačnímu serveru.

Její role přesahuje pouhý přepis; je nedílnou součástí služeb, jako je hlasové vytáčení, hlasová navigace v menu (interaktivní hlasová odezva - IVR), titulkování v reálném čase a hlasové vyhledávání. Přesnost a výkon ASR jsou pro uživatelský zážitek klíčové a jsou ovlivněny faktory, jako je kvalita síťového kodeku (např. AMR, EVS), okolní hluk, variabilita mluvčího a složitost jazykového modelu. Ve specifikacích 3GPP je ASR často diskutováno v kontextu servisních požadavků, mechanismů účtování a API pro vystavení poskytovatelům služeb třetích stran.

## K čemu slouží

ASR bylo zavedeno, aby umožnilo automatizovanou, inteligentní interakci s telekomunikačními sítěmi pomocí přirozené řeči, což představuje posun od tradiční signalizace pomocí tónové volby (DTMF). Před jeho integrací byly interaktivní služby omezeny na rigidní menu systémy založené na vstupech dual-tone multi-frequency (DTMF), které jsou těžkopádné, nepřístupné pro uživatele s pohybovým postižením a neefektivní pro složité dotazy. Rozšíření mobilních zařízení a potřeba bezručního ovládání, zejména v automobilových scénářích a scénářích usnadnění přístupu, poháněly potřebu robustního rozpoznávání řeči podporovaného sítí.

Vytvoření standardizovaných schopností ASR v rámci 3GPP, počínaje Release 6, mělo za cíl poskytnout konzistentní, spolehlivou platformu pro vývojáře služeb napříč různými síťovými operátory a výrobci zařízení. Vyřešilo problém fragmentovaných proprietárních řešení rozpoznávání řeči definováním síťových API a protokolů pro správu zdrojů. To umožnilo vývoj pokročilých hlasových služeb, jako je vytáčení podle vysloveného jména, hlasem ovládané získávání informací a automatizované systémy zákaznické podpory, které mohou škálovat napříč sítí. Dále položilo základy pro budoucí inteligentní služby, včetně integrace s porozuměním přirozenému jazyku pro konverzační rozhraní.

## Klíčové vlastnosti

- Síťový převod řeči na text
- Podpora více jazyků a akustických modelů
- Integrace s IMS a MRF pro zpracování médií
- Rozpoznávání založené na gramatice pro omezené aplikace (např. vytáčení příkazem)
- Vystavení aplikačním serverům prostřednictvím standardizovaných API (např. Parlay X)
- Podpora režimů zpracování v reálném čase a dávkového zpracování

## Definující specifikace

- **TS 22.823** (Rel-16) — IMS enhancements for new real-time communication services
- **TR 22.916** (Rel-19) — Study on Network of Service Robots with Ambient Intelligence
- **TS 23.333** (Rel-19) — MRFC-MRFP Mp Interface Requirements
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TS 23.877** (Rel-6) — Speech Recognition Framework Analysis
- **TS 29.826** (Rel-13) — P-CSCF Restoration Enhancements for WLAN
- **TS 32.299** (Rel-19) — Diameter Charging Applications for 3GPP
- **TS 32.869** (Rel-15) — Diameter Overload Control for Charging Interfaces

---

📖 **Anglický originál a plná specifikace:** [ASR na 3GPP Explorer](https://3gpp-explorer.com/glossary/asr/)
