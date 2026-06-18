---
slug: "nswof"
url: "/mobilnisite/slovnik/nswof/"
type: "slovnik"
title: "NSWOF – Non-Seamless WLAN Offload Function"
date: 2026-01-01
abbr: "NSWOF"
fullName: "Non-Seamless WLAN Offload Function"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/nswof/"
summary: "Funkce jádra sítě 5G, která spravuje směrování provozu v uživatelské rovině na přístupovou síť WLAN na základě politik bez poskytnutí kontinuity relace. Určuje, které toky provozu lze odlehčit na zákl"
---

NSWOF je funkce jádra sítě 5G, která spravuje směrování uživatelského provozu na přístupovou síť WLAN na základě politik bez zachování kontinuity relace; určuje, které toky mají být odlehčeny, na základě politik operátora a stavu sítě.

## Popis

Funkce pro nebezproblémové odlehčení do [WLAN](/mobilnisite/slovnik/wlan/) (Non-Seamless WLAN Offload Function, NSWOF) je síťová funkce zavedená v architektuře systému 5G (5GS) pro správu odlehčování specifického uživatelského datového provozu z jádra 5G na důvěryhodnou bezdrátovou lokální síť (WLAN) nebezproblémovým způsobem. Funguje jako specializovaná funkce řídicí roviny, která interaguje s funkcí řízení politik ([PCF](/mobilnisite/slovnik/pcf/)) a funkcí správy relací ([SMF](/mobilnisite/slovnik/smf/)) k vynucení politik odlehčování. Primární role NSWOF spočívá v vyhodnocení politik operátora, uživatelských předplatitelských dat a informací o přístupové síti v reálném čase (jako je dostupnost a kvalita WLAN), aby rozhodla, zda má být konkrétní relace [PDU](/mobilnisite/slovnik/pdu/) nebo specifický provoz v ní směrován přes přístup WLAN. Tato rozhodnutí jsou následně převedena na pravidla, která jsou předána SMF, a ta nakonec nakonfiguruje funkci uživatelské roviny ([UPF](/mobilnisite/slovnik/upf/)) tak, aby nasměrovala určené toky provozu na rozhraní místní sítě WLAN.

Architektonicky je NSWOF součástí rámce politik 5G a je definována pro podporu funkcí směrování, přepínání a rozdělování přístupového provozu ([ATSSS](/mobilnisite/slovnik/atsss/)), konkrétně však řeší komponentu 'nebezproblémového' odlehčení. S PCF komunikuje přes rozhraní na bázi služeb Nnswof. Při zřízení nebo modifikaci relace PDU se může PCF (pokud je relace způsobilá pro odlehčení) obrátit na NSWOF, aby získalo specifická pravidla pro směrování provozu do WLAN. NSWOF svá rozhodnutí zakládá na předem nakonfigurovaných politikách operátora, které mohou zohledňovat faktory jako typ aplikace (např. streamování vs. na pozadí), aktuální zatížení rádiové přístupové sítě 3GPP (RAN), kvalitu dostupné WLAN a profil předplatitele. Výstupem je sada sad paketových filtrů nebo pravidel směrování, které identifikují IP toky určené k odlehčení.

Jak to funguje, zahrnuje koordinovanou sekvenci. Během zřizování relace PDU obdrží SMF informace o politikách od PCF. Pokud je odlehčení aplikovatelné, může PCF vyvolat NSWOF. NSWOF vrátí specifická pravidla politiky odlehčení. SMF následně vygeneruje pravidla N4 pro UPF, která jí nařídí porovnávat určený provoz (např. na základě 5-tic) a směrovat jej na určenou místní datovou síť ([LADN](/mobilnisite/slovnik/ladn/)) nebo specifické rozhraní N6, které se připojuje k WLAN. Zásadní je, že toto odlehčení je 'nebezproblémové', což znamená, že mezi 5G a WLAN neprobíhá aktivní správa mobility. Pokud UE ztratí připojení k WLAN, jsou tyto odlehčené toky přerušeny a musí být znovu zahájeny aplikací nebo uživatelem přes přístup 5G. NSWOF tak poskytuje centralizovaný, inteligentní kontrolní bod pro správu odlehčování do Wi-Fi v 5G, což jde nad rámec jednodušší metody založené na [APN](/mobilnisite/slovnik/apn/) používané v 4G.

## K čemu slouží

NSWOF byla vytvořena, aby vyvinula a formalizovala nebezproblémové odlehčení do WLAN pro éru 5G. Zatímco jádro EPC v 4G používalo koncept NSWO-APN, architektura jádra 5G na bázi služeb a vylepšené řízení politik vyžadovaly flexibilnější a dynamičtější funkci. NSWOF řeší potřebu podrobných rozhodnutí o směrování provozu v reálném čase, která mohou zohledňovat širší spektrum vstupů nad rámec statického APN, jako jsou okamžité síťové podmínky, povědomí o aplikaci a uživatelsky specifické politiky.

Motivace vychází z pokračujícího významu Wi-Fi jako klíčové doplňkové přístupové technologie v nasazeních 5G, zejména pro pokrytí vnitřních prostor a správu zahlcení provozem. Předchozí přístupy byly relativně statické; NSWO-APN v podstatě vytvářel pevný kanál pro odlehčený provoz. NSWOF jako dedikovaná funkce umožňuje adaptivnější a inteligentnější odlehčování. Operátorům umožňuje implementovat složité politiky, které mohou například odlehčovat pouze v době zahlcení 5G RAN nebo odlehčovat provoz specifických aplikací na základě jejich požadavků na QoS. Tím se řeší problém neefektivního nebo uživatelský zážitek zhoršujícího odlehčování tím, že se z něj stává dynamické, politikami řízené síťové rozhodnutí, nikoli jednoduché statické směrovací pravidlo.

## Klíčové vlastnosti

- Funkce jádra sítě 5G pro odlehčení do WLAN na základě politik bez zachování kontinuity
- Interaguje s PCF přes rozhraní na bázi služeb Nnswof za účelem poskytnutí pravidel směrování
- Rozhoduje o odlehčení na základě politiky operátora, předplatitelských údajů a podmínek přístupové sítě
- Podporuje rámec ATSSS pro směrování provozu přes více přístupů
- Umožňuje dynamická pravidla odlehčení na relaci PDU, nikoli pouze na APN
- Konfiguruje UPF přes SMF ke směrování specifických IP toků na přístup WLAN

## Související pojmy

- [ATSSS – Access Traffic Steering, Switching, and Splitting](/mobilnisite/slovnik/atsss/)
- [PCF – Positioning Calculation Function](/mobilnisite/slovnik/pcf/)
- [SMF – Service Management Function](/mobilnisite/slovnik/smf/)
- [UPF – User Plane Function](/mobilnisite/slovnik/upf/)

## Definující specifikace

- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TS 24.302** (Rel-19) — Access to EPC via non-3GPP networks; Stage 3
- **TS 24.502** (Rel-19) — 5G Core Access via Non-3GPP Networks; Stage 3
- **TS 29.273** (Rel-19) — AAA Protocols for Non-3GPP Access in EPS & 5GS NSWO
- **TS 33.501** (Rel-20) — 5G Security Architecture and Procedures

---

📖 **Anglický originál a plná specifikace:** [NSWOF na 3GPP Explorer](https://3gpp-explorer.com/glossary/nswof/)
