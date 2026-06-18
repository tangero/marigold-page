---
slug: "usd"
url: "/mobilnisite/slovnik/usd/"
type: "slovnik"
title: "USD – User Service Description"
date: 2025-01-01
abbr: "USD"
fullName: "User Service Description"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/usd/"
summary: "Strukturovaný XML dokument popisující charakteristiky, schopnosti a konfiguraci multimediální telefonní služby pro uživatele. Umožňuje personalizaci služby, interoperabilitu mezi různými servisními do"
---

USD je strukturovaný XML dokument, který popisuje multimediální telefonní službu uživatele pro personalizaci, interoperabilitu domén a konzistentní uživatelský zážitek napříč zařízeními.

## Popis

User Service Description (USD) je koncept na servisní vrstvě v architektuře 3GPP, primárně spojovaný s IP Multimedia Subsystem (IMS) a multimediálními telefonními službami. Je definován jako [XML](/mobilnisite/slovnik/xml/) dokument, který obsahuje komplexní popis telefonní služby, jak je zřízena pro konkrétního uživatele. USD není protokol, ale datový model, který zapouzdřuje servisní profil uživatele včetně nastavení služeb, mediálních schopností a konfigurací doplňkových služeb. Typicky je uložen v síťovém úložišti, jako je XML Document Management Server ([XDMS](/mobilnisite/slovnik/xdms/)), a může k němu přistupovat nebo jej spravovat různá síťová entita a uživatelská zařízení.

USD funguje tak, že poskytuje standardizovanou, strojově čitelnou předlohu služby uživatele. Když se zařízení registruje v síti nebo iniciuje službu, může USD načíst, aby pochopilo, jak se samo nakonfigurovat. Například USD může specifikovat preferované kodeky pro audio a video, nastavení pro přesměrování nebo zákaz hovorů, dostupnost funkcí chatu nebo přenosu souborů v rámci hovoru a politiky pro interoperabilitu služeb s legacy okruhově spínanými ([CS](/mobilnisite/slovnik/cs/)) sítěmi. Síť také používá USD k aplikaci konzistentní servisní logiky pro uživatele napříč různými přístupovými sítěmi a relacemi.

Z architektonického hlediska USD interaguje s několika klíčovými komponentami. Telephony Application Server ([TAS](/mobilnisite/slovnik/tas/)) nebo Multimedia Telephony Service (MMTel) [AS](/mobilnisite/slovnik/as/) může odkazovat na USD pro provedení servisní logiky. UE může USD načíst pomocí protokolů jako [HTTP](/mobilnisite/slovnik/http/) nebo [XCAP](/mobilnisite/slovnik/xcap/) (XML Configuration Access Protocol). Klíčovou rolí USD je usnadnění kontinuity služeb a interoperability, zejména mezi IMS-based Voice over LTE (VoLTE) a legacy CS sítěmi prostřednictvím Single Radio Voice Call Continuity ([SRVCC](/mobilnisite/slovnik/srvcc/)) nebo jiných mechanismů. Díky centralizovanému popisu služby se mohou síť i zařízení sladit ve svém chování a zajistit, že funkce jako čekání hovoru, konferenční hovory nebo zpracování médií fungují stejně bez ohledu na podkladovou transportní technologii.

## K čemu slouží

USD byl zaveden v 3GPP Release 8, současně s úplnou standardizací IMS-based multimediální telefonie (MMTel). Jeho vytvoření bylo motivováno složitostí poskytování bohatých, personalizovaných telefonních služeb přes plně IP sítě. Před IMS byly telefonní služby v okruhově spínaných sítích relativně statické a řízené sítí, s omezenou možností uživatelské úpravy. Přechod na paketově spínané, aplikací řízené IMS služby vyžadoval způsob, jak popsat komplexní servisní profil uživatele flexibilním a rozšiřitelným způsobem.

USD řeší problém přenositelnosti služeb a konzistentního uživatelského zážitku. Když uživatelé používají více zařízení (smartphony, tablety, PC) a pohybují se napříč různými přístupovými sítěmi (LTE, Wi-Fi, 3G), USD zajišťuje, že jejich telefonní služba – se všemi personalizovanými funkcemi – je následuje. Také řeší kritickou výzvu interoperability mezi IMS a legacy CS sítěmi během přechodové fáze na plně IP. Definováním servisních schopností v společném popisu může síť bezproblémově mapovat IMS doplňkové služby na jejich CS ekvivalenty (a naopak), čímž udržuje kontinuitu služeb pro uživatele. USD poskytuje nezbytnou abstraktní vrstvu mezi servisní logikou a přístupovou technologií, což zajišťuje budoucí odolnost nasazení služeb.

## Klíčové vlastnosti

- Dokument založený na XML popisující uživatelsky specifická nastavení multimediální telefonní služby
- Umožňuje personalizaci služby a konzistentní zážitek napříč více zařízeními
- Usnadňuje interoperabilitu mezi IMS a legacy okruhově spínanými (CS) servisními doménami
- Uložen a spravován v síťových úložištích jako XDMS
- Přístupný pro UE a aplikační servery pomocí protokolů XCAP nebo HTTP
- Podporuje definici mediálních schopností, doplňkových služeb a komunikačních preferencí

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [MMTEL – Multimedia Telephony Service for IMS](/mobilnisite/slovnik/mmtel/)
- [XCAP – XML Configuration Access Protocol](/mobilnisite/slovnik/xcap/)
- [XDMS – XML Document Management Server](/mobilnisite/slovnik/xdms/)
- [SRVCC – Single Radio Voice Call Continuity](/mobilnisite/slovnik/srvcc/)

## Definující specifikace

- **TS 23.285** (Rel-19) — V2X Architecture Enhancements for LTE
- **TS 23.286** (Rel-19) — V2X Application Enabler Architecture
- **TR 23.785** (Rel-14) — Architecture enhancements for LTE V2X services
- **TS 23.792** (Rel-16) — MBMS API for Mission Critical Services
- **TS 23.795** (Rel-16) — V2X Application Architecture Study
- **TS 24.486** (Rel-19) — V2X Application Enabler (VAE) Protocol Spec
- **TS 24.575** (Rel-19) — UE Pre-configuration for MBS
- **TS 26.237** (Rel-19) — IMS for PSS and MBMS Control
- **TS 26.346** (Rel-19) — MBMS User Services Media Codecs & Protocols
- **TS 26.347** (Rel-19) — MBMS Transport Protocol and API (TRAPI)
- **TS 26.849** (Rel-12) — MBMS Operation on Demand (MooD)
- **TR 26.917** (Rel-19) — TV Service Enhancements over 3GPP
- **TS 31.102** (Rel-19) — USIM Application Specification
- **TS 36.868** (Rel-12) — Study on Group Communication for E-UTRA

---

📖 **Anglický originál a plná specifikace:** [USD na 3GPP Explorer](https://3gpp-explorer.com/glossary/usd/)
