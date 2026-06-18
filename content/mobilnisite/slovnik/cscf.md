---
slug: "cscf"
url: "/mobilnisite/slovnik/cscf/"
type: "slovnik"
title: "CSCF – Call Session Control Function"
date: 2026-01-01
abbr: "CSCF"
fullName: "Call Session Control Function"
category: "Core Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/cscf/"
summary: "CSCF je hlavní uzel IMS (IP Multimedia Subsystem) zodpovědný za řízení SIP relací, autentizaci uživatele a směrování. Spravuje poskytování multimediálních služeb a umožňuje hlas, video a zasílání zprá"
---

CSCF je hlavní uzel IMS zodpovědný za řízení SIP relací, autentizaci uživatele a směrování, který umožňuje multimediální služby jako hlas a video přes IP.

## Popis

Call Session Control Function (CSCF) je základní prvek v architektuře IP Multimedia Subsystem (IMS) podle 3GPP a funguje jako [SIP](/mobilnisite/slovnik/sip/) (Session Initiation Protocol) server. Je zodpovědný za zpracování SIP signalizace pro zřizování, modifikaci a ukončování multimediálních relací, jako je Voice over LTE (VoLTE), videohovory a instant messaging. CSCF není jediná monolitická entita, ale je logicky rozdělena na odlišné funkční typy: Proxy-CSCF ([P-CSCF](/mobilnisite/slovnik/p-cscf/)), Serving-CSCF ([S-CSCF](/mobilnisite/slovnik/s-cscf/)) a Interrogating-CSCF ([I-CSCF](/mobilnisite/slovnik/i-cscf/)), z nichž každý má specifickou roli v cestě řízení relace. P-CSCF je prvním kontaktním bodem pro User Equipment (UE) v rámci IMS, zajišťuje kompresi SIP zpráv, zabezpečení a funguje jako firewall. S-CSCF je centrální uzel, který provádí řízení relací, autentizaci uživatele přes [HSS](/mobilnisite/slovnik/hss/) (Home Subscriber Server) a spouštění služeb na základě uživatelských profilů. I-CSCF funguje jako vstupní bod v síti operátora, dotazuje se HSS, aby určil vhodný S-CSCF pro uživatele, a poskytuje skrytí topologie.

Architektonicky CSCF funguje v řídicí rovině IMS a rozhraní se dalšími klíčovými síťovými funkcemi. Komunikuje s HSS přes rozhraní Cx pro získání uživatelských autentizačních dat a profilů služeb. Pro směrování komunikuje se servery [ENUM](/mobilnisite/slovnik/enum/)/[DNS](/mobilnisite/slovnik/dns/) pro překlad SIP adres a může být rozhraní s Application Servers ([AS](/mobilnisite/slovnik/as/)) přes rozhraní ISC pro provádění přidaných služeb. CSCF také podporuje služby tísňového volání prostřednictvím Emergency-CSCF (E-CSCF), který směruje tísňová volání na správné Public Safety Answering Point (PSAP). Jeho návrh je bezstavový pro škálovatelnost, přičemž stav relace je v případě potřeby udržován externě, což umožňuje vyrovnávání zátěže a vysokou dostupnost ve velkých nasazeních.

Při provozu CSCF zpracovává SIP metody jako INVITE, REGISTER, BYE a SUBSCRIBE. Když uživatel zahájí hovor, P-CSCF přijme SIP INVITE, použije politiky a přepošle jej na S-CSCF přes I-CSCF, je-li to potřeba. S-CSCF autentizuje uživatele, zkontroluje profil služby a směruje požadavek na cíl, případně zapojí AS pro služby jako přesměrování hovoru. Také zpracovává procedury registrace, kdy S-CSCF autentizuje UE a aktualizuje jeho polohu v HSS. CSCF podporuje kvalitu služeb (QoS) interakcí s Policy and Charging Rules Function (PCRF) přes rozhraní Rx pro autorizaci mediálních prostředků. Jeho role se rozšiřuje na zabezpečení, vynucování ochrany integrity a šifrování přes IPSec pro signalizaci mezi UE a P-CSCF a správu prevence podvodů prostřednictvím rozhraní pro zákonné odposlechy.

Vývoj CSCF jej integroval se sítěmi 5G jádra, kde funguje společně s Session Management Function (SMF) a User Plane Function (UPF) pro podporu konvergovaných multimediálních služeb. V 5G je CSCF součástí 5G IMS, umožňuje služby jako Voice over New Radio (VoNR) a zajišťuje zpětnou kompatibilitu s 4G IMS. Také podporuje síťové segmenty (network slicing) tím, že je instancován ve segmentech vyhrazených pro IMS služby, což umožňuje přizpůsobený výkon pro různé případy užití. Implementace CSCF je často virtualizována v cloud-nativních prostředích s využitím kontejnerů a mikroslužeb pro agilitu, což odpovídá přechodu 3GPP na servisně orientovanou architekturu (SBA) v 5G. Tato přizpůsobivost zajišťuje, že CSCF zůstává klíčový pro služby komunikace v reálném čase napříč generacemi.

## K čemu slouží

CSCF byl vytvořen, aby řešil omezení okruhově přepínaných sítí při zpracování multimediálních služeb přes IP. Před IMS mobilní sítě primárně používaly okruhově přepínané domény pro hlas, které byly neefektivní pro datově náročné služby jako video a zasílání zpráv. Vzestup internetových protokolů vyžadoval standardizovaný způsob poskytování IP multimedií s provozovatelskou spolehlivostí, což vedlo 3GPP k zavedení IMS ve verzi 5, s CSCF jako jeho hlavním řídicím prvkem. Řeší problémy jako fragmentované poskytování služeb, nedostatek interoperability mezi operátory a neefektivní správu relací tím, že poskytuje jednotný rámec založený na SIP.

Historicky se přístupy před IMS spoléhaly na proprietární řešení nebo překryvné sítě, které se potýkaly se škálovatelností a integrací. CSCF umožňuje bezproblémovou konvergenci hlasových, video a datových služeb přes plně IP sítě s podporou mobility a roamingu. Řeší klíčové problémy jako autentizace uživatelů napříč doménami, dynamické spouštění služeb a vynucování politik, což bylo v dřívějších systémech náročné. Centralizací řízení relací umožňuje CSCF operátorům rychle nasazovat nové služby, snižovat náklady prostřednictvím IP infrastruktury a uspokojovat rostoucí požadavky spotřebitelů na bohaté komunikační zážitky. Jeho vytvoření bylo motivováno potřebou standardizované, budoucím vývojem odolné architektury, která by mohla podporovat jak dědičné, tak nově vznikající aplikace, a připravila cestu pro služby jako VoLTE a RCS (Rich Communication Services).

## Klíčové vlastnosti

- Řízení SIP relací pro zřizování a správu multimediálních hovorů
- Autentizace a autorizace uživatele prostřednictvím integrace s HSS
- Směrování SIP zpráv mezi UE a síťovými prvky
- Podpora funkčních rolí Proxy, Serving a Interrogating
- Spolupráce s Application Servers pro přidané služby
- Zpracování tísňových hovorů prostřednictvím funkce E-CSCF

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [SIP – Session Initiation Protocol](/mobilnisite/slovnik/sip/)
- [HSS – Home Subscriber Server](/mobilnisite/slovnik/hss/)
- [P-CSCF – Proxy Call Session Control Function](/mobilnisite/slovnik/p-cscf/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.125** (Rel-7) — Flow Based Charging Architecture
- **TS 23.141** (Rel-19) — Presence Service Stage 2 Architecture
- **TS 23.179** (Rel-13) — MCPTT Functional Architecture
- **TS 23.218** (Rel-19) — IMS Call Model Specification
- **TS 23.221** (Rel-19) — 3GPP System Architectural Requirements
- **TS 23.228** (Rel-19) — IMS Stage-2 Service Description
- **TS 23.271** (Rel-19) — LCS Stage 2 Specification
- **TS 23.278** (Rel-19) — CAMEL for IMS Stage 2 Specification
- **TS 23.280** (Rel-20) — Common Architecture for Mission Critical Services
- **TS 23.379** (Rel-20) — MCPTT Functional Architecture
- **TS 23.417** (Rel-7) — IMS Core Component for NGN Architecture
- **TS 23.517** (Rel-8) — IMS Core Component for NGN Architecture
- **TS 23.701** (Rel-12) — WebRTC Access to IMS Architecture Study
- **TS 23.806** (Rel-7) — Voice Call Continuity between CS and IMS
- … a dalších 61 specifikací

---

📖 **Anglický originál a plná specifikace:** [CSCF na 3GPP Explorer](https://3gpp-explorer.com/glossary/cscf/)
