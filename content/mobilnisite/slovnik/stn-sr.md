---
slug: "stn-sr"
url: "/mobilnisite/slovnik/stn-sr/"
type: "slovnik"
title: "STN-SR – Session Transfer Number - Single Radio"
date: 2025-01-01
abbr: "STN-SR"
fullName: "Session Transfer Number - Single Radio"
category: "Mobility"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/stn-sr/"
summary: "STN-SR je jedinečný identifikátor přiřazený uživatelskému zařízení (UE) pro podporu kontinuity hlasového volání (VCC) a konkrétně kontinuity hlasového volání pro jedno rádiové rozhraní (SRVCC). Umožňu"
---

STN-SR je jedinečný identifikátor přiřazený uživatelskému zařízení (UE), který umožňuje síti plynule přenést probíhající hlasové volání z paketové domény LTE/5G do starší okruhově spínané domény pro SRVCC.

## Popis

Session Transfer Number for Single Radio (STN-SR) je kritický datový prvek uložený v uživatelském předplatitelském profilu na serveru [HSS](/mobilnisite/slovnik/hss/) (Home Subscriber Server). V podstatě se jedná o směrovatelné telefonní číslo (ve formátu E.164), které odkazuje na konkrétní síťovou funkci: [MSC](/mobilnisite/slovnik/msc/) Server rozšířený pro [SRVCC](/mobilnisite/slovnik/srvcc/). Když uživatelské zařízení (UE) podporující Voice over LTE (VoLTE) vede hlasové volání a pohybuje se k hranici pokrytí LTE, síť zahájí SRVCC předání služby (handover) do starší okruhově spínané ([CS](/mobilnisite/slovnik/cs/)) sítě, jako je [GERAN](/mobilnisite/slovnik/geran/) nebo [UTRAN](/mobilnisite/slovnik/utran/). STN-SR je klíčem, který tento složitý přenos spouští.

Postup SRVCC funguje následovně: [MME](/mobilnisite/slovnik/mme/) ze zdrojové sítě LTE detekuje potřebu SRVCC předání na základě měřicích hlášení od UE. MME následně načte STN-SR předplatitele z HSS (pokud již není v mezipaměti). MME použije tento STN-SR k navázání signalizačního spojení k cílovému MSC Serveru. To se provádí přes rozhraní Sv, které je definováno speciálně pro SRVCC. STN-SR slouží jako cílová adresa pro tuto signalizaci Sv. MME odešle zprávu SRVCC PS-to-CS Request k MSC Serveru identifikovanému pomocí STN-SR. Tato zpráva obsahuje potřebné podrobnosti o probíhající IMS relaci. MSC Server poté využije své vlastní schopnosti a rozhraní se sítí IMS (přes [SCC](/mobilnisite/slovnik/scc/) AS – IMS Service Centralization and Continuity Application Server) k provedení přenosu relace. Ukotví volání v CS doméně a koordinuje s cílovou rádiovou sítí dokončení předání rádiového spojení UE, a to vše při zachování hlasového volání s minimálním přerušením pro uživatele.

Z architektonického hlediska je STN-SR základním kamenem funkce SRVCC, která byla navržena pro UE s jedním rádiovým transceiverem, které nemůže současně komunikovat se sítěmi LTE a 2G/3G. Bez STN-SR by MME nemělo způsob, jak zjistit, který MSC Server v potenciálně rozsáhlé síti je odpovědný za zpracování SRVCC procedury pro daného předplatitele. Poskytuje mechanismus směrování specifický pro předplatitele pro povel k předání služby. STN-SR je zřízen na úrovni předplatného, což umožňuje flexibilitu – například různí předplatitelé mohou být napojeni na různé, geograficky vhodné MSC Servery pro optimalizovaný výkon předání služby.

## K čemu slouží

STN-SR byl vytvořen k vyřešení klíčové výzvy při nasazování raných sítí LTE: zajištění plynulé hlasové služby dříve, než bylo pokrytí LTE všudypřítomné. LTE bylo navrženo jako čistě paketová síť, přičemž hlas měl být doručován jako VoIP přes IMS (VoLTE). Pokrytí LTE však zpočátku mělo mezery. UE na VoLTE hovoru, které by opustilo pokrytí LTE, by hovor přerušilo, pokud by neexistoval žádný mechanismus kontinuity. Řešení s dvěma rádiovými rozhraní byla možná, ale zvyšovala náklady na zařízení a spotřebu baterie. SRVCC, umožněné právě STN-SR, poskytlo elegantní řešení pro zařízení s jedním rádiovým rozhraním.

Problém, který řešilo, byl nedostatek nativního okruhově spínaného záložního režimu v samotném LTE rádiovém rozhraní. Předchozí mechanismy, jako je CS Fallback (CSFB), vyžadovaly, aby byl hovor nastaven v CS doméně od začátku, pokud bylo UE připojeno k LTE. SRVCC naopak umožnilo, aby hovor vznikal optimálně ve vysokokvalitní doméně VoLTE/IMS a přešel do CS pouze tehdy, když to bylo naprosto nezbytné kvůli rádiovým podmínkám. STN-SR byl tím nezbytným identifikátorem, který umožnil tento dynamický přenos uprostřed hovoru. Propojil MME z paketového jádra, které spravuje událost mobility v LTE, se správnou entitou okruhově spínané domény (MSC Server), která mohla orchestrovat přenos relace s IMS jádrem. To umožnilo operátorům zavádět služby VoLTE s jistotou, že kontinuita hlasové služby může být zachována, čímž se zlepšil uživatelský zážitek a urychlilo přijetí VoLTE.

## Klíčové vlastnosti

- Číslo ve formátu E.164 uložené v předplatitelském profilu na HSS
- Jednoznačně identifikuje MSC Server odpovědný za SRVCC pro daného předplatitele
- Používá se jako cílová adresa pro signalizaci přes rozhraní Sv z MME
- Umožňuje předání služby uprostřed hovoru z VoLTE/IMS do starší okruhově spínané hlasové sítě
- Kritický pro fungování kontinuity hlasového volání pro jedno rádiové rozhraní (SRVCC)
- Podporuje kontinuitu hlasové služby v raných heterogenních nasazeních sítí

## Související pojmy

- [SRVCC – Single Radio Voice Call Continuity](/mobilnisite/slovnik/srvcc/)
- [VCC – Voice Call Continuity](/mobilnisite/slovnik/vcc/)
- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [CSFB – Circuit Switched Fallback](/mobilnisite/slovnik/csfb/)

## Definující specifikace

- **TS 23.009** (Rel-19) — Handover Procedures in PLMNs
- **TS 23.237** (Rel-19) — IMS Service Continuity (ISC) Stage 2
- **TS 24.237** (Rel-19) — IMS Service Continuity Protocol Details
- **TS 24.802** (Rel-12) — IMS II-NNI Traversal Scenario Determination Study
- **TS 29.060** (Rel-19) — GPRS Tunnelling Protocol (GTP) version 1
- **TS 29.274** (Rel-19) — GTPv2-C Control Plane Protocol Specification
- **TS 29.806** (Rel-12) — P-CSCF Restoration Analysis & Solutions
- **TR 29.949** (Rel-19) — VoLTE IMS Roaming Architecture & Procedures

---

📖 **Anglický originál a plná specifikace:** [STN-SR na 3GPP Explorer](https://3gpp-explorer.com/glossary/stn-sr/)
