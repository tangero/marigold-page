---
slug: "aiotf"
url: "/mobilnisite/slovnik/aiotf/"
type: "slovnik"
title: "AIoTF – Ambient IoT Function"
date: 2026-01-01
abbr: "AIoTF"
fullName: "Ambient IoT Function"
category: "IoT"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/aiotf/"
summary: "Funkce Ambient IoT (AIoTF) je síťová funkce zavedená ve specifikaci 3GPP Release 19 pro správu a podporu zařízení Ambient IoT. Jedná se o zařízení s extrémně nízkými náklady a bez baterie, napájená z"
---

AIoTF je síťová funkce zavedená ve specifikaci 3GPP Release 19 pro správu a podporu bezbateriových Ambient IoT zařízení, která poskytuje služby pro jejich registraci, autentizaci a komunikaci.

## Popis

Funkce Ambient IoT (AIoTF) je funkcí základní sítě definovanou v rámci architektury 5G systému (5GS) speciálně pro podporu Ambient IoT, což je nová kategorie IoT zavedená ve specifikaci 3GPP Release 19. Zařízení Ambient IoT se vyznačují extrémní jednoduchostí, ultra nízkou cenou a absencí konvenčního zdroje napájení; fungují tak, že získávají energii z okolních rádiových frekvenčních (RF) signálů, například z buněčných základnových stanic nebo vyhrazených čteček. AIoTF funguje jako centrální síťová entita zodpovědná za správu životního cyklu a konektivity těchto specificky omezených zařízení. Nachází se v rámci řídicí roviny 5G základní sítě (5GC) a komunikuje s dalšími funkcemi základní sítě, jako je funkce správy přístupu a mobility ([AMF](/mobilnisite/slovnik/amf/)) a jednotná správa dat ([UDM](/mobilnisite/slovnik/udm/)), aby poskytla kompletní servisní rámec pro Ambient IoT.

Z architektonického hlediska je AIoTF navržena tak, aby zvládala specifické komunikační vzory a omezení zařízení Ambient IoT. Tato zařízení nemohou iniciovat komunikaci ani provádět složité signalizační procedury jako tradiční uživatelská zařízení (UE). Místo toho fungují v paradigmatu 'čtečka mluví první' nebo v režimu iniciovaném sítí. AIoTF podporuje procedury pro registraci zařízení a správu dosažitelnosti, které tuto asymetrii zohledňují. Klíčovým architektonickým aspektem je role AIoTF při udržování kontextu pro zařízení Ambient IoT, který zahrnuje minimální sadu informací o předplatném a stavu. Tento kontext je nezbytný, protože zařízení samotná nejsou trvale napájena a nemohou ukládat složitý stav. AIoTF může být také zapojena do správy pagingu nebo probouzejících signálů směrovaných ke skupinám zařízení Ambient IoT, aby spustila jejich odezvu, což je proces koordinovaný s rádiovou přístupovou sítí (RAN).

Z procedurálního hlediska AIoTF funguje tak, že komunikuje s AMF, což je první kontaktní bod pro signalizaci iniciovanou zařízením. Když zařízení Ambient IoT získá dostatek energie k napájení své minimální elektroniky, může vyslat jednoduchý signál nebo odpovědět na dotaz sítě. Tento signál je přijat RAN a předán AMF. AMF, která rozpozná typ zařízení, komunikuje s AIoTF za účelem autentizace zařízení a načtení nebo aktualizace jeho kontextu. AIoTF využívá UDM pro data předplatného. Pro downlinkovou komunikaci aplikační server odešle data určená pro zařízení Ambient IoT do 5GC. AIoTF je pak zodpovědná za určení stavu dosažitelnosti zařízení a v případě potřeby za spuštění procedury v RAN (jako je skupinový probouzející signál), aby se zařízení aktivovalo a mohlo data přijmout. Celý tento proces je optimalizován pro minimální signalizační režii a spotřebu energie na straně zařízení.

Role AIoTF je klíčová pro integraci Ambient IoT do ekosystému 5G. Abstrahuje složitost správy těchto pasivních zařízení od ostatních síťových funkcí a aplikačních serverů. Poskytnutím standardizovaných procedur pro registraci, autentizaci a doručování dat umožňuje AIoTF škálovatelné a bezpečné nasazení miliard zařízení Ambient IoT pro případy užití, jako je sledování majetku, chytré senzování a digitální pasy produktů, kde jsou náklady na zařízení a energetická autonomita prvořadé.

## K čemu slouží

AIoTF byla vytvořena, aby řešila zásadní výzvu integrace nové kategorie ultra omezených, bezbateriových IoT zařízení do sítě 5G. Před Release 19 byly standardy 3GPP pro IoT, jako NB-IoT a LTE-M, navrženy pro zařízení s vlastním napájením (bateriemi) a schopností provádět aktivní síťové procedury, jako je náhodný přístup a periodická registrace. Tyto technologie nebyly vhodné pro zařízení získávající energii z okolních RF zdrojů, protože jsou napájena pouze přerušovaně a nemají dostatek energie pro složité obousměrné signalizační sekvence. Požadavek průmyslu na sledování na úrovni jednotlivých položek (např. v logistice, maloobchodě a výrobě) vyžadoval buněčné řešení s téměř nulovou cenou zařízení a neomezenou životností, což motivovalo standardizaci Ambient IoT.

Primární problém, který AIoTF řeší, je poskytnutí síťové řídicí entity pro zařízení, která nemohou spravovat svůj vlastní síťový stav. Tradiční IoT zařízení udržují protokolový kontext se sítí. Zařízení Ambient IoT to kvůli svému přerušovanému provozu nemohou dělat. AIoTF existuje, aby tento kontext udržovala jménem zařízení uvnitř sítě. Řeší problém autentizace zařízení bezstavovým způsobem, spravuje dosažitelnost bez spoléhání se na periodické aktualizace iniciované zařízením a umožňuje efektivní downlinkovou komunikaci prostřednictvím síťových probouzejících mechanismů. Bez vyhrazené funkce, jako je AIoTF, by byly stávající funkce 5G základní sítě zatíženy nestandardními procedurami a optimalizacemi, což by bránilo škálovatelnosti a interoperabilitě.

Historicky podobné koncepty pro správu velmi jednoduchých zařízení existovaly v RFID systémech, ale šlo o izolovaná nebuněčná řešení. Vytvoření AIoTF v rámci 3GPP představuje konvergenci funkcionality podobné RFID s globální buněčnou infrastrukturou. Řeší omezení předchozích nebuněčných přístupů (omezený dosah, proprietární systémy) i předchozích buněčných IoT přístupů (příliš vysoká cena zařízení a spotřeba energie). Definováním AIoTF poskytuje 3GPP standardizovaný, škálovatelný a bezpečný architektonický rámec, který umožňuje Ambient IoT využívat všudypřítomné pokrytí a možnosti správy sítí 5G, čímž odemyká scénáře masivního nasazení.

## Klíčové vlastnosti

- Spravuje registraci a kontext pro bezbateriová zařízení Ambient IoT
- Podporuje síťové procedury komunikace 'čtečka mluví první' iniciované sítí
- Komunikuje s AMF pro autentizaci zařízení a správu dosažitelnosti
- Koordinuje se s RAN pro skupinové probouzející signalizaci směrem k zařízením
- Využívá UDM pro data předplatného předplatitelů Ambient IoT
- Umožňuje efektivní doručování downlinkových dat k přerušovaně napájeným zařízením

## Související pojmy

- [AMF – Access and Mobility Management Function](/mobilnisite/slovnik/amf/)
- [UDM – Unified Data Management](/mobilnisite/slovnik/udm/)
- [NIDD – Non-IP Data Delivery](/mobilnisite/slovnik/nidd/)

## Definující specifikace

- **TS 23.369** (Rel-19) — 5G System Architecture for Ambient IoT
- **TS 24.369** (Rel-19) — AIoT NAS protocol for 5G System
- **TS 28.540** (Rel-20) — 5G Network Resource Model (NRM) Management
- **TS 29.510** (Rel-19) — NRF Service Based Interface Protocol
- **TS 29.518** (Rel-19) — AMF Service Based Interface Protocol
- **TS 32.291** (Rel-19) — Charging Management: Service-Based Interface Protocol
- **TS 33.369** (Rel-19) — Security for AIoT in Isolated Private 5G Networks
- **TS 38.300** (Rel-19) — NG-RAN Overall Description
- **TS 38.401** (Rel-19) — NG-RAN Architecture Specification
- **TS 38.410** (Rel-19) — NG Interface Introduction for NG-RAN to 5GC
- **TS 38.412** (Rel-19) — NG Signalling Transport
- **TS 38.413** (Rel-19) — NG Application Protocol (NGAP)

---

📖 **Anglický originál a plná specifikace:** [AIoTF na 3GPP Explorer](https://3gpp-explorer.com/glossary/aiotf/)
