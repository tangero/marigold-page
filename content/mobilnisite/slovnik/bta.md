---
slug: "bta"
url: "/mobilnisite/slovnik/bta/"
type: "slovnik"
title: "BTA – Background Data Transfer Answer"
date: 2025-01-01
abbr: "BTA"
fullName: "Background Data Transfer Answer"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/bta/"
summary: "BTA je aplikační příkaz Diameter definovaný v 3GPP pro rozhraní Sd. Jedná se o odpověď od funkce detekce provozu (TDF) směrem k funkci pravidel pro účtování a řízení (PCRF) na žádost o přenos dat na p"
---

BTA je příkaz odpovědi Diameter na rozhraní Sd, kterým funkce detekce provozu (TDF) potvrzuje požadavek na politiku od PCRF pro řízení přenosu dat na pozadí.

## Popis

Odpověď na přenos dat na pozadí (BTA) je klíčový příkaz Diameter v architektuře 3GPP Policy and Charging Control (PCC), konkrétně definovaný pro referenční bod Sd (rozhraní) mezi funkcí pravidel pro účtování a řízení (PCRF) a funkcí detekce provozu (TDF). Jako zpráva odpovědi Diameter funguje v rámci transakce požadavek-odpověď iniciované PCRF odesláním žádosti o přenos dat na pozadí ([BTR](/mobilnisite/slovnik/btr/)). BTA nese výsledek požadavku, který udává, zda TDF úspěšně přijala a bude aplikovat požadované politiky pro detekci a řízení přenosů dat na pozadí, nebo zda došlo k chybě.

Technicky je příkaz BTA (Command-Code 8388722) definován v 3GPP TS 29.154. Jedná se o aplikačně specifický příkaz, který rozšiřuje základní protokol Diameter (RFC 6733) pro účely detekce a řízení datových toků služeb v 3GPP. Struktura zprávy zahrnuje standardní hlavičku Diameter s příslušně nastavenými příznaky příkazu (Command Flags) pro zprávu odpovědi, následovanou sekvencí párů atribut-hodnota ([AVP](/mobilnisite/slovnik/avp/)). Tyto AVP přenášejí kontext relace, výsledek požadavku (např. úspěch nebo specifické chybové kódy) a jakékoli relevantní experimentální nebo dodavatelsky specifické AVP definované 3GPP. AVP Session-Id je povinné a musí odpovídat tomu v odpovídající BTR, aby bylo možné korelovat požadavek a odpověď v rámci stejné relace Diameter.

Hlavní úlohou BTA v síti je poskytovat standardizovaný a spolehlivý mechanismus potvrzení v rámci architektury PCC. Když PCRF zřizuje pravidla pro detekci a řízení aplikací na TDF – například pokyny k detekci specifických aplikací pro přenos dat na pozadí (např. aktualizace softwaru, synchronizace v cloudu) a k aplikaci specifických akcí QoS nebo účtování – TDF použije BTA k signalizaci svého souhlasu nebo nahlášení problémů. Úspěšná BTA (s AVP Result-Code udávajícím DIAMETER_SUCCESS) potvrzuje závazek TDF prosadit politiky. Chybová BTA, obsahující příslušný chybový Result-Code (např. DIAMETER_UNABLE_TO_COMPLY, DIAMETER_UNKNOWN_SESSION_ID), informuje PCRF o selhání, což umožňuje PCRF provést nápravnou akci, jako je pokus o opětovné zřízení nebo spuštění alternativní logiky vynucování politik.

Tato zpráva odpovědi je nedílnou součástí udržování stavu a synchronizace mezi PCRF a TDF. Zajišťuje, že rozhodovací bod politik (PCRF) má potvrzený přehled o stavu vynucování politik v detekčním bodě (TDF). Tato smyčka potvrzení je klíčová pro spolehlivé poskytování služeb, přesné účtování za služby dat na pozadí a umožnění pokročilých síťových schopností, jako je sponzorované datové připojení nebo optimalizované řízení provozu pro aplikace na pozadí bez dopadu na uživatelský zážitek z provozu na popředí.

## K čemu slouží

Příkaz BTA byl vytvořen, aby splnil specifickou signalizační potřebu v rámci vyvinuté architektury 3GPP PCC, zejména se zavedením funkce detekce provozu (TDF) jako samostatné entity nebo jako funkčního vylepšení PCEF. Před Rel-13 a formální definicí rozhraní Sd byla detekce a řízení aplikací pro nosiče non-GBR, zejména pro data na pozadí, méně standardizovaná a často řešená proprietárním způsobem v rámci PCEF/brány nebo prostřednictvím boxů s hlubokou kontrolou paketů (DPI) s nestandardními rozhraními. Tento nedostatek standardizace ztěžoval operátorům konzistentní implementaci a zpoplatnění politik pro provoz dat na pozadí, jako je rozlišování mezi provozem iniciovaným uživatelem a automatizovanými přenosy na pozadí od aplikací.

Zavedení standardizovaného rozhraní Sd s jeho dvojicí příkazů [BTR](/mobilnisite/slovnik/btr/)/BTA to vyřešilo tím, že poskytlo otevřený, interoperabilní protokol pro PCRF, aby dynamicky delegovala úkoly detekce a hlášení aplikací na specializovanou TDF. BTA, jako odpověď v této transakci, slouží základnímu účelu dokončení signalizační výměny Diameter a poskytuje spolehlivost. Zajišťuje, že PCRF obdrží explicitní potvrzení, že její instrukce pro zřizování politik byly přijaty a přijaty (nebo zamítnuty) TDF. Toto potvrzení je klíčové pro udržení konzistentního stavu politik napříč síťovými funkcemi a pro spouštění příslušných účtovacích událostí.

BTA navíc umožňuje sofistikované servisní modely. Například operátor může implementovat "sponzorovaná data" pro specifické aktualizace aplikací na pozadí, kde se datové využití neúčtuje koncovému uživateli. PCRF by zřídila odpovídající politiku na TDF prostřednictvím BTR. BTA od TDF potvrdí, že politika je zavedena, což umožní PCRF následně instruovat PCEF/PGW o příslušných pravidlech účtování (rozhraní Gy). Bez potvrzeného handshaku poskytovaného výměnou BTR/BTA by takové koordinované vynucování politik napříč více síťovými prvky bylo nespolehlivé a náchylné k chybám, což by vedlo k nesrovnalostem v účtování a špatné kvalitě služeb.

## Klíčové vlastnosti

- Příkaz odpovědi založený na Diameter (Command-Code 8388722) pro rozhraní Sd
- Poskytuje potvrzení a výsledek pro příkazy žádosti o přenos dat na pozadí (BTR)
- Nese standardní AVP Result-Code Diameter pro indikaci úspěchu nebo konkrétního selhání
- Používá AVP Session-Id ke korelaci s původní BTR v rámci relace
- Umožňuje spolehlivou synchronizaci stavu mezi PCRF a funkcí detekce provozu (TDF)
- Základní pro potvrzení zřizování pravidel detekce a řízení aplikací

## Definující specifikace

- **TS 29.154** (Rel-19) — Nt Reference Point Protocol

---

📖 **Anglický originál a plná specifikace:** [BTA na 3GPP Explorer](https://3gpp-explorer.com/glossary/bta/)
