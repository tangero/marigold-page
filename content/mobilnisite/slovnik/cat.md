---
slug: "cat"
url: "/mobilnisite/slovnik/cat/"
type: "slovnik"
title: "CAT – Card Application Toolkit Runtime Environment"
date: 2026-01-01
abbr: "CAT"
fullName: "Card Application Toolkit Runtime Environment"
category: "Other"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/cat/"
summary: "Standardizované výkonné prostředí na kartách UICC/USIM, které umožňuje bezpečným, standardizovaným aplikacím běžet na mobilních zařízeních. Poskytuje bezpečnou platformu pro přidané služby, jako jsou"
---

CAT je standardizované výkonné prostředí na kartě UICC nebo USIM, které poskytuje bezpečnou platformu pro běh aplikací, jako jsou služby SIM ToolKit, a umožňuje mobilním operátorům nasazovat přidané služby přímo na SIM kartě.

## Popis

Card Application Toolkit (CAT) Runtime Environment je standardizovaný rámec definovaný 3GPP, který poskytuje výkonné prostředí pro aplikace umístěné na UICC (Universal Integrated Circuit Card), což zahrnuje [USIM](/mobilnisite/slovnik/usim/) (Universal Subscriber Identity Module). Toto prostředí je v podstatě virtuální stroj nebo interpret, který běží na mikrokontroléru UICC s omezenými prostředky a umožňuje kartě hostovat a provádět bezpečné, přenosné aplikace nezávislé na mobilním zařízení ([ME](/mobilnisite/slovnik/me/)). Architektura je založena na modelu příkaz-odpověď, kde ME funguje jako terminál, který zobrazuje informace a zachycuje vstup uživatele, zatímco UICC hostuje aplikační logiku a spravuje bezpečná data.

V jádru CAT definuje sadu proaktivních příkazů, které umožňují aplikacím na UICC iniciovat akce na ME, jako je zobrazování nabídek, odesílání [SMS](/mobilnisite/slovnik/sms/), navazování hovorů nebo poskytování lokálních informací, jako je Cell ID. ME naopak posílá terminálové odpovědi a události (jako výběr z nabídky nebo ukončení hovoru) zpět do aplikace na UICC. Tato komunikace probíhá přes standardizované rozhraní mezi UICC a ME, obvykle za použití příkazů [APDU](/mobilnisite/slovnik/apdu/) (Application Protocol Data Unit). Klíčové komponenty zahrnují CAT interpret na UICC, proaktivní obslužný modul UICC v ME a sadu standardizovaných profilů a procedur pro různé typy služeb.

Výkonné prostředí spravuje životní cyklus aplikací, přidělování prostředků a bezpečnostní domény. Aplikace jsou typicky implementovány jako aplety (např. pomocí technologie Java Card), které jsou bezpečně nahrány na UICC. CAT poskytuje mechanismy pro výběr aplikací, jejich aktivaci a komunikaci mezi aplikacemi tam, kde je to podporováno. Zahrnuje funkce pro správu volatilní a nevolatilní paměti, obsluhu časovačů a zpracování událostí uživatelského rozhraní. Bezpečnost je zásadní: aplikace běží v izolovaných bezpečnostních doménách, kryptografické operace se provádějí v rámci bezpečnostního prvku UICC a citlivá data nikdy neopouštějí chráněné prostředí karty.

Role CAT v síti přesahuje základní autentizaci účastníka. Umožňuje služby řízené operátorem, jako jsou nabídky založené na [SIM](/mobilnisite/slovnik/sim/) pro kontrolu zůstatku, doplňování kreditu a aktivaci služeb. Je klíčová pro aplikace typu stroj-stroj (M2M), kde je vyžadována vzdálená správa a provizionování zařízení. V pozdějších vydáních tvoří základ pro pokročilejší bezpečné služby, jako jsou mobilní platby NFC (prostřednictvím bezkontaktních rozhraní), správa zařízení a autentizace pro síťové aplikace. Prostředí zajišťuje, že tyto služby jsou přenositelné mezi různými modely telefonů a operačními systémy, pokud ME podporuje požadované schopnosti CAT.

## K čemu slouží

CAT byl vytvořen, aby řešil omezení dřívějších [SIM](/mobilnisite/slovnik/sim/) karet, které byly čistě pasivními komponentami používanými pouze pro síťovou autentizaci a identifikaci účastníka. S vývojem mobilních sítí potřebovali operátoři způsob, jak nasazovat přidané služby přímo řízené ze strany sítě, bez závislosti na výrobcích telefonů nebo nutnosti instalace softwaru uživatelem. Tradiční SIM neměla standardizovaný způsob, jak provozovat aplikace nebo proaktivně komunikovat s telefonem. CAT poskytl standardizované, bezpečné výkonné prostředí přímo na SIM kartě, čímž ji proměnil z jednoduchého autentizačního modulu na platformu pro poskytování služeb.

Historicky, před CAT, byla jakákoli služba založená na SIM proprietární a nepřenositelná, což uzamykalo operátory u konkrétních dodavatelů karet a omezovalo inovace služeb. Vytvoření CAT ve 3GPP Release 8 (navazující na dřívější specifikace [ETSI](/mobilnisite/slovnik/etsi/)/3GPP pro SIM Application Toolkit) stanovilo jednotný rámec, který zajistil interoperabilitu mezi různými dodavateli UICC a mobilních zařízení. To umožnilo operátorům vyvíjet a nasazovat služby, jako jsou nabídky SIM, aktualizace přes vzduch ([OTA](/mobilnisite/slovnik/ota/)) a aplikace pro bezpečné transakce, které budou konzistentně fungovat na jakémkoli kompatibilním zařízení. Vyřešilo to problém přenositelnosti služeb a vytvořilo důvěryhodné výkonné prostředí uvnitř již zabezpečené SIM karty.

Dále CAT řešil rostoucí potřebu bezpečných služeb přesahujících hlas a SMS. Jak se mobilní zařízení začala používat pro bankovnictví, platby a identitu, bezpečnostní prvek SIM karty poskytoval ideální hardwarově zakotvený bod důvěry. CAT to umožnil tím, že poskytl runtime, kde mohou citlivé aplikace provádět izolovaně, provádět kryptografické operace a spravovat bezpečné úložiště. Tento účel se významně rozšířil s příchodem NFC a mobilních peněženek, kde se aplikace založené na CAT staly bezpečnostním prvkem pro bezkontaktní transakce. Také umožnil vzdálenou správu zařízení M2M, kde UICC mohlo hostovat aplikace pro konfiguraci zařízení, diagnostiku a provizionování služeb bez fyzického přístupu.

## Klíčové vlastnosti

- Standardizované proaktivní příkazy UICC pro iniciaci akcí na mobilním zařízení
- Bezpečné výkonné prostředí pro aplety v rámci hardwarové bezpečnosti UICC
- Přenositelný aplikační rámec nezávislý na operačním systému telefonu
- Podpora více současných aplikací s izolovanými bezpečnostními doménami
- Mechanismy pro výběr aplikací, jejich aktivaci a obsluhu událostí
- Schopnosti pro interakci s uživatelským rozhraním, stahování dat a přístup k lokálním informacím

## Související pojmy

- [USIM – Universal Subscriber Identity Module](/mobilnisite/slovnik/usim/)
- [APDU – Application Protocol Data Unit](/mobilnisite/slovnik/apdu/)

## Definující specifikace

- **TS 22.173** (Rel-20) — IMS Multimedia Telephony Service Definition
- **TS 22.182** (Rel-19) — Customized Alerting Tone (CAT) Service Requirements
- **TS 22.810** (Rel-13) — Enhanced Calling Information Presentation Requirements
- **TR 22.878** (Rel-18) — Technical Report on 5G Timing Resiliency
- **TR 22.982** (Rel-19) — Customized Alerting Tone Service Requirements
- **TS 24.008** (Rel-19) — 3GPP TS 24008: Core Network Protocols
- **TS 24.182** (Rel-19) — Customized Alerting Tones (CAT) Protocol
- **TS 24.186** (Rel-19) — IMS Data Channel applications
- **TS 24.615** (Rel-19) — Communication Waiting (CW) Service Protocol
- **TR 26.917** (Rel-19) — TV Service Enhancements over 3GPP
- **TS 29.163** (Rel-19) — Interworking between 3GPP IM CN and CS networks
- **TS 29.165** (Rel-19) — Inter-IMS Network to Network Interface (NNI)
- **TS 29.364** (Rel-19) — IMS AS Service Data Descriptions
- **TS 29.827** (Rel-16) — Policy and Charging for Volume Based Charging
- **TS 29.864** (Rel-8) — Application Server Service Data Definition for IMS Telephony
- … a dalších 7 specifikací

---

📖 **Anglický originál a plná specifikace:** [CAT na 3GPP Explorer](https://3gpp-explorer.com/glossary/cat/)
