---
slug: "lphap"
url: "/mobilnisite/slovnik/lphap/"
type: "slovnik"
title: "LPHAP – Low Power and High Accuracy Positioning"
date: 2025-01-01
abbr: "LPHAP"
fullName: "Low Power and High Accuracy Positioning"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/lphap/"
summary: "Funkce 3GPP zavedená v Release 18 pro umožnění energeticky úsporných a přesných lokalizačních služeb pro IoT a spotřebitelská zařízení. Optimalizuje polohovací procedury, aby minimalizovala spotřebu e"
---

LPHAP je funkce 3GPP Release 18, která umožňuje energeticky úsporné a přesné lokalizační služby pro IoT a spotřebitelská zařízení optimalizací procedur za účelem minimalizace spotřeby energie při dosahování polohových určení s vysokou přesností.

## Popis

Low Power and High Accuracy Positioning (LPHAP) je služební prvek definovaný v 3GPP Release 18, který řeší dvojí požadavky na přesné určení polohy a prodlouženou životnost baterie uživatelského zařízení (UE), zejména senzorů internetu věcí (IoT), nositelné elektroniky a chytrých telefonů. Z architektonického hlediska LPHAP zahrnuje vylepšení napříč UE, rádiovou přístupovou sítí (RAN) a 5G jádrem sítě (5GC), konkrétně v rámci funkce správy polohy ([LMF](/mobilnisite/slovnik/lmf/)) a funkce správy přístupu a mobility ([AMF](/mobilnisite/slovnik/amf/)). Základním principem je optimalizace signalizačního toku a měřicích procedur pro určování polohy za účelem snížení aktivního rádiového času a režie zpracování pro UE, čímž se šetří energie, při současném využívání vysoce přesných polohovacích metod, jako je Assisted Global Navigation Satellite System ([A-GNSS](/mobilnisite/slovnik/a-gnss/)), Observed Time Difference of Arrival ([OTDOA](/mobilnisite/slovnik/otdoa/)) a vícebuněčné měření doby zpátečního letu (RTT).

Jak LPHAP funguje, zahrnuje několik klíčových mechanismů. Za prvé zavádí efektivnější správu polohovacích relací, což umožňuje síti konfigurovat delší periodicitu pro hlášení polohy nebo spouštět měření pouze na základě specifických událostí, a tím omezit častou signalizaci. Za druhé vylepšuje doručování pomocných dat do UE; LMF může poskytnout bohatší, předem vypočítaná pomocná data (např. efemeridy satelitů, identity buněk) v jediném přenosu, což umožní UE provést rychlejší zachycení satelitů nebo buněčná měření s menší výpočetní náročností. Za třetí LPHAP podporuje určování polohy s asistencí postranního spoje (sidelink), kde může UE získat měření související s polohou od blízkých zařízení přes rozhraní PC5, což potenciálně snižuje její vlastní využití [GNSS](/mobilnisite/slovnik/gnss/) nebo buněčného rádiového rozhraní. UE také může po polohovacích relacích rychleji přejít do stavů s nízkou spotřebou (jako [RRC](/mobilnisite/slovnik/rrc/)_IDLE nebo RRC_INACTIVE) a síť může naplánovat polohovací referenční signály (PRS) energeticky úsporným způsobem, například jejich sdružením do méně symbolů nebo použitím širšího rozestupu subnosných.

Klíčové komponenty zahrnují LMF, která řídí procedury LPHAP a vybírá vhodné polohovací metody na základě požadované přesnosti a požadavků na úsporu energie; UE, která implementuje vylepšené měřicí schopnosti a stavy úspory energie; a gNB, které vysílá optimalizované PRS a podporuje efektivní správu kontextu UE. Úlohou LPHAP je integrovat určování polohy jako udržitelnou službu v rámci sítí 5G-Advanced, což umožní nové komerční a bezpečnostně kritické aplikace bez kompromisů v životnosti baterie zařízení. Je to klíčový prvek pro masivní nasazení IoT, kde zařízení mohou potřebovat hlásit svou polohu periodicky po celé roky na jedno nabití baterie, a zároveň splňovat přísné požadavky na přesnost aplikací, jako je navigace dronů, autonomní vozidla a průmyslová automatizace.

## K čemu slouží

LPHAP byl vytvořen k vyřešení inherentního konfliktu mezi dosahováním služeb určování polohy s vysokou přesností a udržováním nízké spotřeby energie v mobilních a IoT zařízeních. Před Release 18 se 3GPP polohovací funkce, jako je LTE Positioning Protocol ([LPP](/mobilnisite/slovnik/lpp/)) a NR positioning, zaměřovaly primárně na přesnost a latenci, často na úkor energetické účinnosti UE. Časté polohovací relace, nepřetržité hlášení měření a složité výpočty pro techniky jako [A-GNSS](/mobilnisite/slovnik/a-gnss/) mohly rychle vybít baterie, což je činilo nepraktickými pro zařízení pro nepřetržité sledování nebo spotřebitelskou nositelnou elektroniku. LPHAP to řeší optimalizací celého pracovního postupu určování polohy z pohledu spotřeby energie.

Mezi hnací problémy patří rostoucí poptávka po přesné poloze v IoT sledování majetku, nositelných zdravotních monitorech a tísňových službách (např. E911), kde jsou zařízení často omezena baterií. Stávající řešení buď obětovala přesnost pro úsporu energie, nebo vyžadovala časté dobíjení, což omezovalo škálovatelnost nasazení. LPHAP je motivován potřebou podporovat 5G vertikály, jako jsou chytrá města, logistika a rozšířená realita, které vyžadují jak přesné určování polohy, tak dlouhou životnost zařízení. Také je v souladu s širšími cíli 3GPP v oblasti energetické účinnosti sítě a podpory zařízení s redukovanými schopnostmi (RedCap).

Historicky se spotřeba energie pro určování polohy řešila roztříštěně, pomocí některých proprietárních řešení nebo řešení na aplikační vrstvě. LPHAP tyto optimalizace standardizuje v rámci frameworku 3GPP, čímž zajišťuje interoperabilitu napříč dodavateli a sítěmi. Zavedením síťově řízených režimů úspory energie pro určování polohy a vylepšením doručování pomocných dat umožňuje zařízením dosahovat přesnosti na úrovni centimetrů až metrů při provozu na baterie po celé roky, což otevírá nové komerční případy užití a zlepšuje uživatelský zážitek u služeb založených na poloze v 5G-Advanced a dalších generacích.

## Klíčové vlastnosti

- Optimalizuje signalizaci a správu relací pro určování polohy za účelem snížení aktivního času a spotřeby energie UE.
- Vylepšuje doručování pomocných dat pro A-GNSS a buněčné určování polohy pro urychlení určení a snížení výpočetní zátěže UE.
- Podporuje určování polohy s asistencí postranního spoje (sidelink) pro využití měření z blízkých zařízení, čímž snižuje využití rádiového rozhraní jednotlivého UE.
- Umožňuje síťovou konfiguraci energeticky účinných periodicit určování polohy a hlášení spouštěných událostmi.
- Integruje se s funkcí správy polohy (LMF) v 5GC pro komplexní řízení určování polohy s ohledem na spotřebu energie.
- Usnadňuje využití stavů UE s nízkou spotřebou (RRC_INACTIVE) během polohovacích procedur pro úsporu energie.

## Související pojmy

- [LPP – LTE Positioning Protocol](/mobilnisite/slovnik/lpp/)
- [LMF – Location Management Function](/mobilnisite/slovnik/lmf/)
- [A-GNSS – Assisted Global Navigation Satellite Systems](/mobilnisite/slovnik/a-gnss/)
- [OTDOA – Observed Time Difference Of Arrival](/mobilnisite/slovnik/otdoa/)

## Definující specifikace

- **TS 23.273** (Rel-19) — 5G Location Services Stage 2 Architecture
- **TS 29.503** (Rel-19) — UDM Service Based Interface Stage 3
- **TS 29.515** (Rel-19) — Ngmlc Service Based Interface Protocol
- **TS 29.518** (Rel-19) — AMF Service Based Interface Protocol
- **TS 29.572** (Rel-19) — Nlmf Service Based Interface Stage 3
- **TR 38.859** (Rel-18) — Technical Report

---

📖 **Anglický originál a plná specifikace:** [LPHAP na 3GPP Explorer](https://3gpp-explorer.com/glossary/lphap/)
