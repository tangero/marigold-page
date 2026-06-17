---
slug: "macf"
url: "/mobilnisite/slovnik/macf/"
type: "slovnik"
title: "MACF – Multiple Association Control Function"
date: 2025-01-01
abbr: "MACF"
fullName: "Multiple Association Control Function"
category: "Core Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/macf/"
summary: "Funkce v jádrové síti v IP Multimedia Subsystem (IMS), která spravuje více současných servisních asociací pro jednoho uživatele. Koordinuje SIP sezení, registrace a odběry, čímž umožňuje komplexní slu"
---

MACF je funkce v jádrové síti v IMS, která spravuje více současných servisních asociací pro uživatele, koordinuje SIP sezení, registrace a odběry, aby umožnila služby jako čekání na hovor a konferenční hovory.

## Popis

Multiple Association Control Function (MACF) je logická funkce v architektuře IP Multimedia Subsystem (IMS), definovaná v kontextu Service Centralization and Continuity (SCC) a dalších pokročilých telefonních služeb. Jejím hlavním úkolem je spravovat a řídit více asociací – jako jsou SIP dialogy, odběry a registrace – které se vztahují k jedné IMS Public User Identity uživatele. 'Asociace' představuje vazbu mezi uživatelem a konkrétní instancí služby nebo komunikačním sezením. MACF funguje jako centrální koordinační bod, který zajišťuje konzistentní zacházení s těmito více, potenciálně interagujícími asociacemi.

Provozně je MACF často implementována uvnitř nebo v úzké součinnosti se Serving-Call Session Control Function (S-CSCF). Když je uživatel zapojen do více současných sezení (např. hlasového hovoru, sdílení videa a sezení zasílání zpráv) nebo vyvolal služby jako Call Waiting nebo Communication Diversion, MACF poskytuje logiku pro správu stavu a interakcí mezi těmito sezeními. Například ve scénáři Call Waiting by MACF spravovala signalizaci pro přepnutí aktivního hovoru do režimu hold a připojení čekajícího hovoru, čímž zajišťuje, že SIP signalizace pro obě sezení je z pohledu sítě správně koordinována. Zpracovává větvení a slučování SIP požadavků, spravuje časovače a vynucuje servisní logiku, která závisí na stavu více asociací.

Klíčové komponenty, které s MACF interagují, jsou IMS terminály uživatele (UE), S-CSCF a Application Servers ([AS](/mobilnisite/slovnik/as/)) poskytující konkrétní služby. Funkce MACF interpretuje initial Filter Criteria (iFC) a interaguje s AS pro provedení servisní logiky. Její role je klíčová pro umožnění sofistikované, na síť orientované kontroly služeb, kterou IMS poskytuje, a přesahuje tak jednoduché point-to-point hovory. Díky centralizované kontrole více asociací MACF předchází stavům soutěže, zajišťuje konzistentní chování služeb a umožňuje implementaci komplexních funkcí definovaných ve specifikacích 3GPP jako TS 24.523 (IMS Multimedia Telephony Service). Je základním prvkem pro to, aby se IMS stalo skutečnou platformou pro poskytování služeb.

## K čemu slouží

MACF byla vytvořena, aby řešila omezení dřívějších telefonních a VoIP systémů při zpracování komplexních, stavových uživatelských interakcí napříč více současnými komunikačními sezeními. Tradiční okruhově přepínané sítě a základní SIP proxy dokázaly efektivně spravovat jednu hovorovou větev, ale měly potíže s funkcemi, které vyžadovaly koordinaci mezi více sezeními pro jednoho uživatele, jako je čekání na hovor, konzultační hold nebo multimediální konferenční hovory. To často vedlo k nepředvídatelnému chování, konfliktům služeb nebo vyžadovalo příliš složitou logiku v koncovém uživatelském zařízení.

V rámci architektury IMS se ukázala potřeba centralizované řídicí funkce pro spolehlivé poskytování pokročilých telefonních a multimediálních služeb, které standard slibuje. MACF poskytuje síti inteligenci k pochopení celkového servisního kontextu uživatele. To řeší klíčové problémy: brání tomu, aby jedna služba (např. přesměrování hovoru) nesprávně interferovala s jinou (např. probíhajícím konferenčním hovorem), a umožňuje síti nabízet konzistentní chování služeb bez ohledu na schopnosti uživatelského zařízení. Centralizací této kontroly v jádru sítě může operátor aktualizovat a spravovat servisní logiku, což umožňuje rychlé nasazení nových funkcí pro více sezení a zajišťuje interoperabilitu mezi síťovými prvky a uživatelskými zařízeními různých výrobců.

## Klíčové vlastnosti

- Centralizovaná kontrola a koordinace více SIP dialogů, odběrů a registrací pro jednu uživatelskou identitu.
- Umožňuje pokročilé telefonní služby jako Communication Waiting, Hold/Retrieve a Multi-party konferenční hovory.
- Interpretuje a provádí servisní logiku na základě initial Filter Criteria (iFC) ve spolupráci s Application Servers.
- Spravuje interakce stavů sezení, aby předcházela konfliktům a zajistila konzistentní chování služeb.
- Často implementována jako logická funkce uvnitř S-CSCF v jádrové síti IMS.
- Kritická pro Service Centralization and Continuity (SCC) a IMS Multimedia Telephony (MMTel).

## Související pojmy

- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [MMTEL – Multimedia Telephony Service for IMS](/mobilnisite/slovnik/mmtel/)

## Definující specifikace

- **TS 24.523** (Rel-19) — NGCN-NGN Interconnection Scenarios
- **TS 29.078** (Rel-19) — CAMEL Phase 4 CAP Specification

---

📖 **Anglický originál a plná specifikace:** [MACF na 3GPP Explorer](https://3gpp-explorer.com/glossary/macf/)
