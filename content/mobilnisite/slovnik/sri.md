---
slug: "sri"
url: "/mobilnisite/slovnik/sri/"
type: "slovnik"
title: "SRI – Send Routeing Information"
date: 2025-01-01
abbr: "SRI"
fullName: "Send Routeing Information"
category: "Core Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/sri/"
summary: "Procedura jádra sítě používaná k získání směrovacích informací o mobilním účastníkovi, jako je adresa aktuálně obsluhující MSC nebo SGSN. Je klíčová pro doručení hovoru, směrování SMS a služby založen"
---

SRI je procedura jádra sítě používaná k získání směrovacích informací o mobilním účastníkovi, jako je adresa aktuální obsluhující MSC, za účelem umožnění doručení hovoru a směrování SMS.

## Popis

Send Routeing Information (SRI) je kritická [MAP](/mobilnisite/slovnik/map/) (Mobile Application Part) procedura definovaná v architektuře jádra sítě 3GPP, primárně využívaná v sítích GSM, UMTS a vyvinutých paketových jader. Funguje mezi síťovými entitami, jako je [HLR](/mobilnisite/slovnik/hlr/) (Home Location Register), [VLR](/mobilnisite/slovnik/vlr/) (Visitor Location Register), [MSC](/mobilnisite/slovnik/msc/) (Mobile Switching Center) a [SGSN](/mobilnisite/slovnik/sgsn/) (Serving [GPRS](/mobilnisite/slovnik/gprs/) Support Node). Procedura je vyvolána, když síťový uzel, například Gateway MSC ([GMSC](/mobilnisite/slovnik/gmsc/)) pro příchozí hovor nebo [SMS](/mobilnisite/slovnik/sms/) Interworking MSC (SMS-IWMSC) pro doručení SMS, potřebuje určit aktuálně obsluhující uzel pro konkrétní Mobile Station International Subscriber Directory Number (MSISDN). Dotazující se entita odešle zprávu SRI k účastníkovu HLR. HLR, který spravuje účastníkovský profil a aktuální informace o poloze, odpoví směrovacími údaji, které typicky zahrnují MSC Number (MSC-Number) nebo adresu SGSN. Tato odpověď může také obsahovat dodatečné informace, jako je stav účastníka a případné instrukce pro přesměrování.

Procedura SRI je základní pro správu mobility a navazování relací. Pro služby s přepojováním okruhů, jako jsou hlasové hovory, použije GMSC číslo MSC obdržené v odpovědi SRI k směrování hovoru prostřednictvím ISUP (ISDN User Part) Initial Address Message (IAM) ke správné obsluhující MSC. Pro služby s přepojováním paketů nebo SMS přes GPRS je poskytnuta směrovací adresa pro SGSN. HLR může také indikovat, zda je účastník nedostupný (např. odpojený) nebo má aktivní služby přesměrování hovoru, což mění logiku směrování. Procedura podporuje jak synchronní, tak asynchronní režimy provozu a je zabezpečena pomocí MAP bezpečnostních mechanismů.

Z architektonického hlediska je SRI součástí sady protokolů MAP, která pro přenos v legacy sítích používá SS7 (Signaling System No. 7) nebo SIGTRAN (Signaling Transport), a v pozdějších nasazeních vyvinutých paketových jader rozhraní založená na Diameteru. Její role přesahuje základní doručování hovorů; je nedílnou součástí zákonného odposlechu, služeb polohy (LCS) a dotazů na přenosnost čísel. V moderních sítích, i při přechodu na all-IP jádra a IMS (IP Multimedia Subsystem), zůstávají SRI a její vyvinuté protějšky relevantní pro interoperabilitu s legacy doménami s přepojováním okruhů a pro určité administrativní a regulační funkce.

## K čemu slouží

Procedura SRI byla vytvořena k vyřešení základního problému lokalizace mobilního účastníka v globálně distribuované, buněčné síti. Ve fixní telefonii je telefonní číslo staticky asociováno s fyzickou linkou a ústřednou. V mobilních sítích se může účastník pohybovat kamkoli, což činí dynamické směrování nezbytným. Před standardizovanými procedurami, jako je SRI, neexistovala efektivní, standardizovaná metoda, jak by bránová ústředna mohla dotazovat domovskou databázi účastníka (HLR), aby našla jeho aktuálně obsluhující ústřednu. To by vedlo k nedoručeným hovorům, neefektivnímu zaplavování sítě dotazy na polohu nebo závislosti na nestandardních proprietárních mechanismech.

Její zavedení ve Release 4 formalizovalo klíčovou komponentu signalizační roviny GSM/UMTS, což umožnilo škálovatelné, automatizované doručování hovorů a zpráv. Vyřešila omezení spočívající v nutnosti předchozí znalosti polohy účastníka tím, že tuto inteligenci centralizovala v HLR. Procedura umožňuje síti oddělit funkci řízení hovoru (v GMSC) od databáze polohy účastníka (HLR), čímž dodržuje jasné funkční oddělení, které zvyšuje škálovatelnost, spolehlivost sítě a schopnost zavádět nové služby, jako je přesměrování hovoru a roaming. Je základním kamenem pro umožnění bezproblémového národního a mezinárodního roamingu, neboť poskytuje standardizovanou metodu dotazování, která funguje napříč infrastrukturami různých síťových operátorů.

## Klíčové vlastnosti

- Získá směrovací adresu aktuálně obsluhující MSC nebo SGSN pro dané MSISDN
- Standardizovaná MAP (Mobile Application Part) procedura definovaná ve specifikacích 3GPP
- Klíčová pro směrování při navazování příchozích hovorů a doručování SMS
- Vrací informace o stavu účastníka (např. připojený, odpojený, blokovaný)
- Podporuje dotazování jak pro domény s přepojováním okruhů, tak paketů
- Umožňuje síťové funkce, jako je dotaz HLR na přesměrování hovoru

## Související pojmy

- [HLR – Home Location Register](/mobilnisite/slovnik/hlr/)
- [MAP – Mobile Application Protocol](/mobilnisite/slovnik/map/)
- [MSC – Mobile Services Switching Centre](/mobilnisite/slovnik/msc/)
- [GMSC – Gateway Mobile Services Switching Centre](/mobilnisite/slovnik/gmsc/)
- [MSISDN – Mobile Station International Subscriber Directory Number](/mobilnisite/slovnik/msisdn/)

## Definující specifikace

- **TS 23.018** (Rel-19) — Basic call handling in 3GPP CS domain
- **TS 23.066** (Rel-19) — Mobile Number Portability Technical Realization
- **TS 23.087** (Rel-19) — User-to-User Signalling (UUS) Stage 2
- **TS 23.682** (Rel-19) — 3GPP TS 23682: MTC Architecture Enhancements
- **TR 23.737** (Rel-17) — Satellite Access in 5G Architecture Study
- **TS 23.840** (Rel-7) — SMS Inter-PLMN Architecture Study
- **TS 24.259** (Rel-19) — Personal Network Management (PNM) Protocol Details
- **TR 37.910** (Rel-19) — 5G SRIT and NR RIT Self-Evaluation Report
- **TS 38.213** (Rel-19) — NR Physical Layer Control Procedures
- **TS 38.321** (Rel-19) — NR MAC Protocol Specification
- **TR 38.802** (Rel-14) — Study on New Radio Access Technology Physical Layer Aspects
- **TS 38.821** (Rel-16) — NR Support for Non-Terrestrial Networks
- **TS 38.824** (Rel-16) — NR URLLC Physical Layer Enhancements Study
- **TR 38.889** (Rel-16) — NR-based access to unlicensed spectrum study
- **TR 38.912** (Rel-19) — Study on New Radio Access Technology

---

📖 **Anglický originál a plná specifikace:** [SRI na 3GPP Explorer](https://3gpp-explorer.com/glossary/sri/)
