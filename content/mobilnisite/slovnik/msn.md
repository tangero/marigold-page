---
slug: "msn"
url: "/mobilnisite/slovnik/msn/"
type: "slovnik"
title: "MSN – Multiple Subscriber Number"
date: 2025-01-01
abbr: "MSN"
fullName: "Multiple Subscriber Number"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/msn/"
summary: "Služební funkce umožňující jednomu uživatelskému zařízení (UE) nebo IMS předplatnému přiřazení více telefonních čísel (MSISDN). Umožňuje oddělené identity pro různé účely, například samostatná čísla p"
---

MSN je služební funkce umožňující jedinému IMS předplatnému nebo zařízení přiřadit více telefonních čísel, což umožňuje oddělené identity, například samostatná čísla pro pracovní a osobní použití na jednom zařízení.

## Popis

Multiple Subscriber Number (MSN) je služební schopnost, která umožňuje, aby jedna identita účastníka (propojená s [IMSI](/mobilnisite/slovnik/imsi/) nebo IMS Public User Identity) byla asociována s více než jedním adresářovým číslem E.164 ([MSISDN](/mobilnisite/slovnik/msisdn/)). Architektonicky to zahrnuje koordinaci mezi [HSS](/mobilnisite/slovnik/hss/)/[UDM](/mobilnisite/slovnik/udm/), které ukládají asociaci více MSISDN k jednomu uživatelskému profilu, a Telephony Application Server (TAS) nebo jinou služební logikou v IMS core. Když je uskutečněn hovor na jedno z MSN čísel, síť (např. [MSC](/mobilnisite/slovnik/msc/) Server pro okruhově spínané hovory nebo IMS core pro IP hovory) použije signalizační informace, jako je Called Party Number, k identifikaci cílového MSISDN. Následně dotazuje HSS/UDM, aby tento MSISDN přeložil na odpovídající účastníkovo IMSI nebo [IMPU](/mobilnisite/slovnik/impu/). Klíčovým technickým mechanismem je mapovací a směrovací logika, která zachází s každým MSISDN jako se samostatným adresovatelným koncovým bodem, který se nakonec přeloží na stejné fyzické nebo logické uživatelské zařízení. Služební logika na TAS může být přizpůsobena pro každý MSISDN; například mohou být aplikována různá pravidla pro přesměrování hovoru, hlasové pozdravy nebo tarify v závislosti na tom, které číslo bylo voláno. V kontextu IMS je každý MSISDN typicky asociován s odlišným Tel URI (např. tel:+1234567890) a tyto mohou být implicitně nebo explicitně registrovány jako Public User Identity propojené se stejnou private user identity a služebním profilem. To umožňuje síti prezentovat příslušnou identitu (volané číslo) volané straně a aplikovat služební logiku specifickou pro tuto 'linku' nebo identitu.

## K čemu slouží

Služba MSN byla vyvinuta pro uspokojení poptávky po možnosti, aby jediné zařízení podporovalo více telefonních identit pro různé role nebo kontexty, například samostatná čísla pro osobní život, práci a faxovou linku. Před touto standardizovanou funkcí museli uživatelé nosit více zařízení nebo SIM karet. Problém, který řeší, je správa identit a diferenciace služeb na jediném předplatném. Umožňuje operátorům nabízet flexibilní služební balíčky, kde uživatel může mít pro každé číslo odlišné účtování, směrování hovorů a doplňkové služby (jako hlasová schránka), přičemž vše je účtováno na jediný účet. Její vznik byl motivován potřebami firemních uživatelů a vývojem směrem ke konvergovaným službám. Poskytuje síťově-centrické řešení pro správu více identit, které je plynulejší než spoléhání se na aplikace na straně zařízení nebo více SIM karet, a čistě se integruje s existující síťovou směrovací a služební řídicí infrastrukturou.

## Klíčové vlastnosti

- Umožňuje asociaci více MSISDN s jediným IMSI/IMPU
- Umožňuje odlišné směrování hovorů a služební logiku pro každé telefonní číslo
- Podporuje diferencované účtování, přesměrování hovorů a hlasovou schránku pro každé MSN
- Síťově založená funkce, nezávislá na schopnostech zařízení
- Integruje se s HSS/UDM pro mapování identit a načítání služebního profilu
- Aplikovatelná v okruhově spínané i IMS telekomunikační doméně

## Související pojmy

- [MSISDN – Mobile Station International Subscriber Directory Number](/mobilnisite/slovnik/msisdn/)
- [IMSI – International Mobile Subscriber Identity](/mobilnisite/slovnik/imsi/)
- [IMPU – IP Multimedia Public User Identity](/mobilnisite/slovnik/impu/)
- [HSS – Home Subscriber Server](/mobilnisite/slovnik/hss/)
- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)

## Definující specifikace

- **TS 29.163** (Rel-19) — Interworking between 3GPP IM CN and CS networks
- **TS 33.108** (Rel-19) — LI Handover Interface Specification

---

📖 **Anglický originál a plná specifikace:** [MSN na 3GPP Explorer](https://3gpp-explorer.com/glossary/msn/)
