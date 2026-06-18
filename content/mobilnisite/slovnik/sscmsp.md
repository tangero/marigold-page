---
slug: "sscmsp"
url: "/mobilnisite/slovnik/sscmsp/"
type: "slovnik"
title: "SSCMSP – Session and Service Continuity Mode Selection Policy"
date: 2026-01-01
abbr: "SSCMSP"
fullName: "Session and Service Continuity Mode Selection Policy"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/sscmsp/"
summary: "Politika v 5G Core (5GC), která určuje vhodný mód kontinuity relace a služby (Session and Service Continuity, SSC) pro PDU relaci. Politiku aplikuje SMF s přihlédnutím k datům o předplatném, síťovým p"
---

SSCMSP je politika (policy) 5G Core aplikovaná funkcí SMF za účelem výběru vhodného módu kontinuity relace a služby (Session and Service Continuity) pro PDU relaci na základě údajů o předplatném, síťových politik a schopností UE.

## Popis

Politika výběru módu kontinuity relace a služby (Session and Service Continuity Mode Selection Policy, SSCMSP) je funkce síťového řízení v rámci architektury 5G Core (5GC), standardizovaná v 3GPP TS 23.501. Řídí výběr módu kontinuity relace a služby (Session and Service Continuity, [SSC](/mobilnisite/slovnik/ssc/)) pro relaci protokolové datové jednotky (Protocol Data Unit, [PDU](/mobilnisite/slovnik/pdu/)) zřízenou uživatelským zařízením (User Equipment, UE). SSC mód definuje chování kontinuity kotvícího bodu uživatelské roviny (User Plane Function, [UPF](/mobilnisite/slovnik/upf/)) relace – tedy bodu, kde se relace připojuje k datové síti (Data Network, [DN](/mobilnisite/slovnik/dn/)) – během mobility UE. SSCMSP je klíčová politika aplikovaná funkcí správy relací (Session Management Function, [SMF](/mobilnisite/slovnik/smf/)) během procedur zřízení nebo modifikace PDU relace.

Logika této politiky sídlí ve SMF, která funguje jako bod vynucení politiky. SMF vyhodnocuje více vstupů, aby učinila rozhodnutí o výběru SSC módu. Mezi klíčové vstupy patří: údaje o předplatném SSC módu účastníka získané ze správy jednotných dat (Unified Data Management, [UDM](/mobilnisite/slovnik/udm/)), politiky síťového operátora nakonfigurované ve funkci řízení politik (Policy Control Function, [PCF](/mobilnisite/slovnik/pcf/)) a hlášené schopnosti a preference UE. Na základě těchto vstupů SMF vybere jeden ze tří definovaných SSC módů. SSC mód 1 zachovává stejný kotvící bod PDU relace (UPF), i když se UE pohybuje, a nabízí tak nejvyšší úroveň kontinuity relace. SSC mód 2 umožňuje síti dočasně ukončit starou PDU relaci a okamžitě zřídit novou s novým kotvícím UPF, což poskytuje krátké přerušení konektivity. SSC mód 3 umožňuje staré a nové PDU relaci (s různými kotvícími body) po určitou dobu koexistovat, což umožňuje UE plynule přepnout datový tok.

Po výběru SMF vynutí SSC mód nakonfigurováním příslušného UPF a pravidel N4 relace a poskytne vybraný mód UE prostřednictvím signalizace [NAS](/mobilnisite/slovnik/nas/) SM. SSCMSP umožňuje systému 5G přizpůsobit kontinuitu relace potřebám různých služeb. Například kritický IoT senzor může používat SSC mód 1 pro zachování konstantní IP adresy, zatímco aplikace pro synchronizaci souborů na pozadí může efektivně využívat SSC mód 2 nebo 3. Tento přístup řízený politikami je klíčovým prvkem pro síťové segmenty (network slicing), protože různé segmenty mohou aplikovat různé SSCMSP, aby splnily své specifické smlouvy o úrovni služeb pro mobilitu a kontinuitu.

## K čemu slouží

SSCMSP byla vytvořena, aby řešila složitý kompromis mezi bezproblémovou kontinuitou služby a optimálním směrováním/lokalizací ve vysoce flexibilní, službami založené architektuře 5G. V předchozích generacích mobilních sítí byla kontinuita IP adresy často vázána na konkrétní síťový kotvící bod (např. PGW v 4G), což mohlo při vzdáleném pohybu UE od jeho kotvícího bodu vést k neoptimálním, 'trombónovitým' datovým cestám. Distribuovaná architektura UPF v 5G umožňuje přemístění kotvícího bodu, ale to může narušit IP adresu relace.

Účelem SSCMSP je poskytnout rámec politik, který tento kompromis inteligentně spravuje pro každou relaci individuálně. Řeší problém 'univerzálního' řízení mobility. Různé služby mají zcela odlišné požadavky: komunikace v reálném čase potřebuje nepřerušené relace (SSC mód 1), zatímco mnoho datových služeb může tolerovat krátké přerušení pro výhodu efektivnější datové cesty (SSC mód 2/3). SSCMSP umožňuje síťovému operátorovi definovat politiky na základě typu služby, úrovně předplatného, síťového segmentu a aktuálních síťových podmínek. To umožňuje efektivní využití síťových zdrojů, snižuje latenci tím, že umožňuje přemístění kotvícího bodu blíže k UE, a přitom stále garantuje požadovanou úroveň kontinuity pro prémiové služby. Je to základní prvek pro plnění různorodých výkonnostních slibů 5G, od rozšířeného mobilního širokopásmového připojení (enhanced Mobile Broadband, eMBB) až po ultra-spolehlivé komunikace s nízkou latencí (Ultra-Reliable Low-Latency Communications, URLLC).

## Klíčové vlastnosti

- Výběr mezi SSC módem 1, 2 a 3 pro PDU relaci řízený politikou
- Vynucováno funkcí správy relací (SMF) během zřízení/modifikace relace
- Konsoliduje vstupy z dat o předplatném (UDM), politik operátora (PCF) a schopností UE
- Umožňuje správu kontinuity specifickou pro službu v souladu s požadavky síťových segmentů (network slicing)
- Přímo ovlivňuje umístění a případné přemístění kotvícího bodu PDU relace (UPF)
- Signalizováno UE, aby bylo informováno o aplikovaném módu kontinuity relace

## Definující specifikace

- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2

---

📖 **Anglický originál a plná specifikace:** [SSCMSP na 3GPP Explorer](https://3gpp-explorer.com/glossary/sscmsp/)
