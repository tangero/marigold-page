---
slug: "5g-tmsi"
url: "/mobilnisite/slovnik/5g-tmsi/"
type: "slovnik"
title: "5G-TMSI – 5G Temporary Mobile Subscription Identifier"
date: 2025-01-01
abbr: "5G-TMSI"
fullName: "5G Temporary Mobile Subscription Identifier"
category: "Identifier"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/5g-tmsi/"
summary: "5G-TMSI je dočasný identifikátor přidělený AMF pro UE za účelem ochrany soukromí a efektivního signalizačního provozu. Jednoznačně identifikuje UE v rámci konkrétní sady AMF a slouží k ochraně trvaléh"
---

5G-TMSI je dočasný identifikátor přidělený AMF pro UE, který ji jednoznačně identifikuje v rámci konkrétní sady AMF, čímž chrání trvalý SUPI na rádiovém rozhraní z důvodu ochrany soukromí a efektivního signalizačního provozu.

## Popis

5G-TMSI (5G Temporary Mobile Subscription Identifier) je základní dočasný identifikátor používaný v síti 5G Core (5GC) k jednoznačné a dočasné identifikaci uživatelského zařízení (UE) během jeho registrace a aktivních relací. Jde o 32bitovou hodnotu přidělenou funkcí pro správu přístupu a mobility ([AMF](/mobilnisite/slovnik/amf/)) UE po úspěšném provedení procedur registrace nebo služebního požadavku. Primární architektonickou rolí 5G-TMSI je sloužit jako lokální alias v rámci obsluhující AMF a její přidružené sady AMF, což síti umožňuje odkazovat se na bezpečnostní kontext a profil účastníka UE bez opakovaného přenosu jeho trvalého, globálně jednoznačného [SUPI](/mobilnisite/slovnik/supi/) (Subscription Permanent Identifier) přes rádiové rozhraní, což je klíčové bezpečnostní a soukromostní opatření.

Provozně je 5G-TMSI vytvářen a spravován AMF. Když se UE poprvé registruje v síti bez platného 5G-TMSI (např. při počátečním připojení nebo po přesunu do nové oblasti sledování), použije pro identifikaci svůj SUPI nebo jeho variantu chráněnou soukromím ([SUCI](/mobilnisite/slovnik/suci/)). Po úspěšné autentizaci a registraci AMF přidělí nové 5G-TMSI a doručí jej UE v zabezpečené [NAS](/mobilnisite/slovnik/nas/) (Non-Access Stratum) zprávě. Následně UE pro většinu signalizačních procedur, jako jsou služební požadavky, periodické aktualizace registrace nebo aktualizace registrace při mobilitě, zahrne toto 5G-TMSI do [RRC](/mobilnisite/slovnik/rrc/) (Radio Resource Control) a NAS zpráv. AMF použije přijaté 5G-TMSI k efektivnímu načtení kontextu UE ze své lokální databáze.

Struktura tohoto identifikátoru, ačkoli jde o 32bitový řetězec, je členěna tak, aby kódovala směrovací informace. Nejvýznamnější bity mohou indikovat ID sady AMF a ukazatel AMF, což pomáhá rádiové přístupové síti (RAN) v oblasti oznamování založené na RAN ([RNA](/mobilnisite/slovnik/rna/)) nebo během stavu RRC Inactive směrovat počáteční zprávu od UE ke správné AMF v rámci poolu. Tato směrovací schopnost je klíčovou součástí efektivního řízení mobility a relací a zabraňuje nutnosti rozesílacího volání (broadcast paging) napříč všemi AMF v poolu. Platnost 5G-TMSI je vázána na registrační stav UE; síť jej může přidělit znovu při opětovné registraci, mobilitě mezi AMF nebo pro periodickou obnovu jako opatření pro zvýšení soukromí.

V širším 5G systému funguje 5G-TMSI ve spojení s dalšími identifikátory, jako je [5G-GUTI](/mobilnisite/slovnik/5g-guti/) (5G Globally Unique Temporary Identifier), který poskytuje globálně směrovatelnou dočasnou identitu. 5G-TMSI tvoří nejméně významných 32 bitů 5G-GUTI. Zatímco 5G-GUTI se používá pro mobilitu mezi AMF a mezi [PLMN](/mobilnisite/slovnik/plmn/), 5G-TMSI je optimalizováno pro efektivitu signalizace uvnitř sady AMF. Jeho role je klíčová pro snížení signalizační zátěže, umožnění rychlého načítání kontextu a zásadní ochranu soukromí uživatele minimalizací přenosu trvalých přihlašovacích údajů, což z něj činí základní kámen bezpečného přístupu a řízení mobility v 5G.

## K čemu slouží

5G-TMSI bylo vytvořeno za účelem řešení kritických nedostatků předchozích mobilních generací, zejména vystavování dlouhodobých identit účastníků na rádiovém rozhraní. V před-5G systémech, jako je LTE, se sice používalo TMSI (Temporary Mobile Subscriber Identity), ale celková struktura identifikátorů a soukromostní mechanismy byly méně robustní. 5G-TMSI jako součást rámce 5G-GUTI poskytuje strukturovanější a bezpečnější systém dočasné identifikace navržený pro architekturu založenou na službách (service-based architecture) 5GC.

Primární problém, který řeší, je ochrana soukromí uživatele. Trvalý identifikátor účastníka (SUPI) nesmí být nikdy přenášen v čitelné podobě přes nezabezpečené rádiové spoje. Používáním často se měnícího 5G-TMSI pro většinu signalizačních interakcí je SUPI chráněn před odposloucháváním, čímž se zabraňuje sledování a profilování účastníka. Tím se řeší rostoucí regulatorní a spotřebitelské požadavky na zvýšené soukromí. Dále řeší problémy s efektivitou sítě. 5G-TMSI se zakódovanými směrovacími informacemi AMF umožňuje RAN rychle směrovat požadavky na připojení ke správné AMF bez rozsáhlého dotazování, čímž se snižují prodlevy při navazování spojení a signalizační zátěž sítě, což je zásadní pro podporu masivního počtu IoT zařízení a ultra-spolehlivých komunikací s nízkou latencí.

Historicky existovaly dočasné identifikátory ve 2G/3G/4G, ale oddělená architektura 5G (oddělující AMF od SMF) a podpora nových stavů, jako je RRC Inactive, vyžadovaly propracovanější přístup. 5G-TMSI je navrženo tak, aby bezproblémově fungovalo v rámci struktury 5G-GUTI a podporovalo efektivní mobilitu napříč pooly AMF a PLMN, což je scénář častější v hustých a heterogenních nasazeních sítí 5G. Jeho vytvoření bylo motivováno potřebou škálovatelného, bezpečného a efektivního schématu správy identit, které podporuje rozmanité případy užití 5G, od vylepšeného mobilního širokopásmového připojení až po hromadné komunikace mezi stroji, aniž by bylo ohroženo výkon nebo bezpečnost.

## Klíčové vlastnosti

- 32bitový dočasný identifikátor přidělený AMF
- Chrání trvalý SUPI před odhalením na rádiovém rozhraní
- Kóduje ID sady AMF a ukazatel AMF pro efektivní směrování
- Tvoří nejméně významnou část 5G-GUTI
- Používá se pro identifikaci UE v NAS a RRC signalizaci
- Periodicky nebo při mobilitě obnovován pro zvýšení soukromí

## Související pojmy

- [5G-GUTI – 5G Globally Unique Temporary Identifier](/mobilnisite/slovnik/5g-guti/)
- [SUPI – Subscription Permanent Identifier](/mobilnisite/slovnik/supi/)
- [AMF – Access and Mobility Management Function](/mobilnisite/slovnik/amf/)
- [NAS – Non-Access Stratum](/mobilnisite/slovnik/nas/)

## Definující specifikace

- **TS 24.501** (Rel-19) — 5G NAS Protocols Specification
- **TS 24.890** (Rel-16) — 5G NAS Protocol for 5GS Stage 3

---

📖 **Anglický originál a plná specifikace:** [5G-TMSI na 3GPP Explorer](https://3gpp-explorer.com/glossary/5g-tmsi/)
