---
slug: "pinapp"
url: "/mobilnisite/slovnik/pinapp/"
type: "slovnik"
title: "PINAPP – Personal IoT Network Application"
date: 2026-01-01
abbr: "PINAPP"
fullName: "Personal IoT Network Application"
category: "IoT"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/pinapp/"
summary: "PINAPP označuje podporu aplikační vrstvy pro osobní sítě IoT (Personal IoT Networks) zavedenou ve specifikaci 3GPP Release 18. Umožňuje uživatelům vytvářet a spravovat vlastní lokalizované sítě IoT sl"
---

PINAPP je aplikační funkcionalita vrstvy ze specifikace 3GPP Release 18, která umožňuje uživatelům vytvářet, spravovat a ovládat lokalizované sítě IoT pro jejich osobní zařízení.

## Popis

Podpora aplikační vrstvy pro osobní sítě IoT (Personal IoT Network Application, PINAPP) je funkcionalita 3GPP zavedená v Release 18, která usnadňuje funkce aplikační vrstvy pro osobní sítě IoT ([PIN](/mobilnisite/slovnik/pin/)). Osobní síť IoT (Personal IoT Network) je uživatelsky orientovaná, lokalizovaná síť složená z IoT zařízení vlastněných a spravovaných jednotlivcem, například zařízení pro chytrou domácnost, nositelná elektronika nebo osobní senzory. PINAPP poskytuje aplikační rámec a schopnosti pro objevování, konfiguraci, řízení a orchestraci služeb mezi těmito zařízeními. Architektonicky PINAPP funguje nad transportní a síťovou vrstvou, využívá stávající konektivitu 3GPP (např. prostřednictvím 5G nebo LTE), ale přidává aplikačně specifické protokoly a [API](/mobilnisite/slovnik/api/). Zahrnuje mechanismy pro objevování a registraci zařízení v rámci osobní sítě, popis služeb a zveřejnění schopností zařízení, aplikační řízení zabezpečení a ochrany soukromí specifické pro uživatelskou doménu a správu životního cyklu (zřizování, aktualizace, odebrání). PINAPP může využívat standardizované aplikační protokoly nebo rozhraní definovaná ve specifikacích, jako jsou 23.542 (Service Enabler Architecture) a 23.700 (System Architecture), pro komunikaci se zařízeními a se síťovými funkcemi, jako je funkce pro správu PIN (PIN Management Function). Role PINAPP v síti spočívá v propojení personalizovaného ekosystému IoT zařízení se službami 3GPP core sítě, což uživatelům umožňuje vytvářet integrované zážitky a umožňuje poskytovatelům služeb nabízet nadstavbové aplikace nad samotnou konektivitou. Funguje tak, že umožňuje aplikaci (např. aplikaci v chytrém telefonu nebo cloudové službě) komunikovat s PIN Management Function pro získání kontextu o osobní síti a následně přímo interagovat se zařízeními pomocí zpráv na aplikační vrstvě.

## K čemu slouží

PINAPP byl vytvořen v Release 18 jako odpověď na rostoucí trend osobních ekosystémů IoT, kde uživatelé mají více připojených zařízení vytvářejících privátní síť. Předchozí zaměření 3GPP na IoT bylo více na rozsáhlém průmyslovém IoT (IoT) nebo obecné konektivitě zařízení a postrádalo standardizovanou podporu pro uživatelsky orientované aplikační řízení a integraci služeb napříč osobními zařízeními. PINAPP řeší problém roztříštěných zážitků s osobním IoT tím, že poskytuje standardizovaný aplikační rámec umožňující bezproblémové objevování, správu a vzájemné propojení osobních zařízení. Umožňuje nové spotřebitelské služby, jako je jednotné ovládání chytré domácnosti nebo personalizované monitorování zdraví napříč nositelnou elektronikou, a to s využitím spolehlivosti a zabezpečení sítí 3GPP. Jeho vytvoření bylo motivováno potřebou rozšířit roli 3GPP do aplikační domény IoT a zajistit, aby osobní sítě mohly být efektivně integrovány se službami a správou mobilních sítí.

## Klíčové vlastnosti

- Podpora na aplikační vrstvě pro objevování a registraci zařízení v osobní síti IoT
- Popis služeb a zveřejnění schopností pro osobní IoT zařízení
- Uživatelsky orientované řízení zabezpečení a ochrany soukromí na aplikační úrovni
- Integrace s PIN Management Function pro síťový kontext
- Správa životního cyklu (zřizování, aktualizace) aplikací pro osobní IoT
- Využití standardizovaných aplikačních protokolů a API (např. ze specifikace 23.542)

## Související pojmy

- [5G – Fifth Generation Mobile Network](/mobilnisite/slovnik/5g/)

## Definující specifikace

- **TS 23.542** (Rel-20) — Application layer support for Personal IoT Network
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TS 24.583** (Rel-19) — Application Layer Support for Personal IoT Network
- **TR 26.806** (Rel-18) — Technical Report on Smartly Tethering AR Glasses
- **TS 29.583** (Rel-19) — PINAPP Stage 3 Protocol for PIN-9 Interface

---

📖 **Anglický originál a plná specifikace:** [PINAPP na 3GPP Explorer](https://3gpp-explorer.com/glossary/pinapp/)
