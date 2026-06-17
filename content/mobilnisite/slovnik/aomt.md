---
slug: "aomt"
url: "/mobilnisite/slovnik/aomt/"
type: "slovnik"
title: "AOMT – Application Originated Mobile Terminated"
date: 2025-01-01
abbr: "AOMT"
fullName: "Application Originated Mobile Terminated"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/aomt/"
summary: "AOMT umožňuje aplikacím zahájit komunikační relace směrem k mobilním zařízením, aniž by zařízení muselo nejprve navázat spojení. Umožňuje síťově iniciované doručování služeb pro UE v úsporných stavech"
---

AOMT je mechanismus 3GPP, který umožňuje aplikacím zahájit komunikační relace směrem k mobilním zařízením, čímž umožňuje síťově iniciované doručování služeb uživatelskému zařízení v úsporných režimech.

## Popis

Application Originated Mobile Terminated (AOMT, komunikace směrem k mobilnímu zařízení iniciovaná aplikací) je služební schopnost definovaná 3GPP, která umožňuje aplikacím, typicky umístěným na aplikačních serverech mimo síť 3GPP nebo uvnitř síťových funkcí, zahájit komunikační relace směrem k uživatelskému zařízení (UE), které může být v různých úsporných režimech. Na rozdíl od tradiční komunikace směrem k mobilnímu zařízení, která vyžaduje, aby bylo UE v připojeném režimu nebo pravidelně monitorovalo kanály pro paging, poskytuje AOMT mechanismy, díky nimž může síť efektivně kontaktovat UE nacházející se v idle nebo inactive stavu, zejména ta nakonfigurovaná s rozšířeným nespojitým příjmem (eDRX) nebo režimem úspory energie (PSM) pro IoT aplikace.

Architektura podporující AOMT zahrnuje několik klíčových síťových funkcí. Funkce pro vystavení služebních schopností (SCEF) v 4G nebo funkce pro vystavení sítě ([NEF](/mobilnisite/slovnik/nef/)) v 5G slouží jako vstupní bod pro externí aplikace žádající o služby AOMT. Tyto funkce autentizují a autorizují žádosti aplikací a následně komunikují se základními síťovými funkcemi, jako je entita správy mobility ([MME](/mobilnisite/slovnik/mme/)) v 4G nebo funkce správy přístupu a mobility ([AMF](/mobilnisite/slovnik/amf/)) v 5G. Když potřebuje aplikace kontaktovat UE, odešle žádost k SCEF/NEF, která následně spustí příslušné procedury základní sítě za účelem lokalizace a zavolání (paging) UE, a to i v případě, že je v hlubokém spánkovém režimu s prodlouženými cykly monitorování.

Technická realizace AOMT zahrnuje sofistikovanou správu časování a stavů. Pro UE nakonfigurovaná s funkcemi úspory energie si síť udržuje přehled o vzorcích dostupnosti UE, včetně cyklů eDRX a hodnot časovače aktivního stavu PSM. Když dorazí žádost AOMT, síť určí optimální čas pro zavolání (paging) UE na základě jejích nakonfigurovaných monitorovacích oken. To vyžaduje přesnou synchronizaci mezi znalostí sítě o spánkových vzorcích UE a skutečným chováním UE, která je udržována prostřednictvím registračních procedur a periodických aktualizací.

AOMT podporuje různé modely doručování služeb včetně doručování dat směrem k mobilnímu zařízení, síťově iniciovaných žádostí o služby a notifikací spouštěných aplikací. Systém zahrnuje mechanismy pro řešení selhání doručení s možnostmi opakovaných pokusů a expiračních časovačů. Pro IoT zařízení je AOMT navrženo tak, aby minimalizovalo dopad na životnost baterie optimalizací procedur pagingu a síťových politik. Služba zahrnuje parametry kvality služby a bezpečnostní aspekty, které zajišťují, že komunikaci mohou iniciovat pouze autorizované aplikace, a to s náležitými kontrolami autentizace a autorizace na více úrovních.

## K čemu slouží

AOMT bylo vytvořeno za účelem řešení zásadní výzvy, kterou je umožnění efektivní síťově iniciované komunikace směrem k energeticky omezeným IoT zařízením a mobilním terminálům pracujícím v pokročilých úsporných režimech. Tradiční komunikace směrem k mobilnímu zařízení předpokládala, že zařízení jsou buď připojena, nebo pravidelně monitorují pagingové kanály, ale IoT nasazení využívající eDRX a PSM zavedla prodloužená spánková období v rozmezí od minut až po hodiny, což učinilo konvenční pagingové mechanismy neefektivní. Bez schopností AOMT by aplikace musely čekat, až se zařízení probudí a sama zahájí kontakt, což by pro mnohé případy užití IoT, jako jsou nouzová upozornění, vzdálené aktualizace konfigurace nebo doručování příkazů v reálném čase, vytvořilo nepřijatelnou latenci.

Historický kontext vývoje AOMT spočívá ve vývoji standardů 3GPP pro podporu masivních IoT nasazení. Když Release 13 zavedl vylepšenou komunikaci typu stroj-stroj (eMTC) a úzkopásmový IoT (NB-IoT) s pokročilými funkcemi úspory energie, stalo se zřejmým, že stávající mechanismy pro kontaktování zařízení jsou nedostatečné. Předchozí přístupy buď vyžadovaly, aby zařízení zůstávala v připojených stavech (což vybíjí baterii), nebo ukládaly nepraktickou latenci pro síťově iniciovanou komunikaci. AOMT poskytuje standardizované rozhraní a procedury, které umožňují aplikacím spolehlivě kontaktovat zařízení při respektování jejich konfigurace úspory energie.

Nad rámec IoT řeší AOMT širší požadavky 5G na efektivní doručování služeb ve scénářích, kde zařízení tráví většinu času v energeticky úsporných stavech. Umožňuje nové modely služeb, kde je síťově iniciovaná komunikace nezbytná, jako jsou push notifikace, aktualizace softwaru, nouzová upozornění a vzdálená správa zařízení. Standardizací těchto schopností v Release 16 a novějších zajišťuje 3GPP interoperabilitu mezi síťovým vybavením, zařízeními a aplikačními servery od různých výrobců, čímž vytváří konzistentní ekosystém pro síťově spouštěné doručování služeb.

## Klíčové vlastnosti

- Umožňuje aplikacím zahájit komunikaci směrem k UE v úsporných režimech
- Podporuje zařízení nakonfigurovaná s eDRX a PSM pro IoT aplikace
- Poskytuje standardizovaná rozhraní prostřednictvím SCEF (4G) a NEF (5G)
- Zahrnuje mechanismy pro řešení selhání doručení a politiky opakování
- Zachovává bezpečnost prostřednictvím autentizace a autorizace žádostí aplikací
- Optimalizuje procedury pagingu za účelem minimalizace dopadu na životnost baterie UE

## Související pojmy

- [NEF – Network Exposure Function](/mobilnisite/slovnik/nef/)
- [MTC – Machine Type Communications](/mobilnisite/slovnik/mtc/)

## Definující specifikace

- **TS 22.262** (Rel-19) — MSGin5G Service Requirements
- **TS 23.554** (Rel-19) — MSGin5G Service Application Architecture

---

📖 **Anglický originál a plná specifikace:** [AOMT na 3GPP Explorer](https://3gpp-explorer.com/glossary/aomt/)
