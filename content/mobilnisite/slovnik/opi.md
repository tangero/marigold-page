---
slug: "opi"
url: "/mobilnisite/slovnik/opi/"
type: "slovnik"
title: "OPI – Offload Preference Indicator"
date: 2025-01-01
abbr: "OPI"
fullName: "Offload Preference Indicator"
category: "Mobility"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/opi/"
summary: "Indikátor preference převedení provozu (OPI) je parametr používaný sítí k ovlivnění výběru přístupové sítě uživatelským zařízením (UE), zejména mezi sítěmi 3GPP (např. LTE, 5G) a ne-3GPP (např. Wi-Fi)"
---

OPI je síťový parametr, který ovlivňuje výběr mezi 3GPP a ne-3GPP přístupovými sítěmi v uživatelském zařízení za účelem řízení směrování provozu a vyrovnávání zátěže na základě politik operátora.

## Popis

Indikátor preference převedení provozu (OPI) je parametr poskytovaný sítí, používaný v rámci frameworku funkce pro zjišťování a výběr přístupové sítě ([ANDSF](/mobilnisite/slovnik/andsf/)) a později vyvinutých politik k usměrňování chování uživatelského zařízení (UE) při výběru mezi různými rádiovými přístupovými technologiemi. Jeho primární rolí je indikovat preferenci sítě pro převedení datového provozu ze sítí 3GPP (jako LTE nebo NR) na sítě ne-3GPP (nejčastěji Wi-Fi). OPI není přímý příkaz, ale vlivná hodnota, kterou UE používá spolu s dalšími politikami a prahovými hodnotami pro konečné rozhodnutí o výběru přístupu.

Technicky je OPI doručeno do UE prostřednictvím řídicích objektů, jako jsou politiky ANDSF (specifikované v TS 24.312) nebo v pozdějších 5G systémech prostřednictvím politik UE z funkce řízení politik ([PCF](/mobilnisite/slovnik/pcf/)). Obvykle se jedná o celočíselnou hodnotu. Logika rozhodování UE, často implementovaná v jeho operačním systému nebo firmwaru modemu, vyhodnocuje OPI vůči lokálně nakonfigurovaným prahům nebo jiným přijatým pravidlům politik. Například síť může nastavit vysokou hodnotu OPI pro přetíženou buňku, čímž silně povzbuzuje UE s Wi-Fi schopností k připojení k dostupné Wi-Fi síti. Naopak nízká hodnota OPI může indikovat preferenci, aby UE zůstalo nebo se vrátilo na síť 3GPP, například proto, že je mobilní síť málo vytížená nebo nabízí specifickou službu (jako hlas) s vyšší kvalitou.

OPI spolupracuje s dalšími parametry, jako je [WLANSP](/mobilnisite/slovnik/wlansp/) (politika výběru [WLAN](/mobilnisite/slovnik/wlan/)) a RANSP (politika výběru RAN). Klíčovým mechanismem je jeho interakce s Indikátorem možnosti převedení provozu. Síť může označit určité toky provozu (na základě [APN](/mobilnisite/slovnik/apn/) nebo [DNN](/mobilnisite/slovnik/dnn/)) jako 'převeditelné' nebo 'nepřeveditelné'. Preference OPI se typicky vztahuje pouze na převeditelný provoz. Pro kritické služby jako IMS hlas je může síť označit jako nepřeveditelné, což zajišťuje jejich setrvání v síti 3GPP bez ohledu na hodnotu OPI. Tato detailní kontrola umožňuje operátorům implementovat sofistikované strategie směrování provozu, jako je převedení provozu pro prohlížení webu s nejlepším úsilím na Wi-Fi v hustě obydlených městských oblastech, zatímco provoz citlivý na latenci (např. hraní her) zůstává na řízeném 5G připojení.

## K čemu slouží

OPI bylo zavedeno, aby řešilo rostoucí potřebu inteligentního směrování provozu mezi heterogenními sítěmi, konkrétně explozi dostupnosti Wi-Fi spolu s všudypřítomným pokrytím 3GPP. Rané implementace ve smartphonech často používaly jednoduchý, uživatelem řízený nebo zařízením řízený výběr Wi-Fi (např. 'připojit se ke známému [SSID](/mobilnisite/slovnik/ssid/)'), což mohlo vést ke špatnému uživatelskému zážitku – například když se zařízení drželo velmi slabého Wi-Fi signálu místo přepnutí na silný LTE signál – a k neefektivnímu využití síťových zdrojů. Operátoři postrádali standardizovaný, sítí řízený mechanismus, jak toto rozhodnutí ovlivnit.

Účelem OPI je poskytnout operátorovi nástroj založený na politikách pro optimalizaci celkového výkonu sítě a uživatelského zážitku. Řeší problém nekontrolovaného převedení provozu tím, že umožňuje síti vyjádřit své podmínky zatížení a preference. To umožňuje klíčové případy užití, jako je vyrovnávání zátěže: během špičky na stadionu může síť nastavit vysoké OPI, aby povzbudila UE k využití nasazené Wi-Fi sítě, čímž uleví přetížení na buněčném RAN. Také podporuje kontinuitu služeb; operátor může použít nízké OPI k nasměrování UE zpět na mobilní síť, když opouští oblast pokrytí Wi-Fi, aby se předešlo náhlému výpadku. Centralizací této logiky směrování v síťových politikách namísto algoritmech v zařízení mohou operátoři implementovat konzistentní, celosíťové strategie pro správu provozu napříč různými typy zařízení a operačními systémy.

## Klíčové vlastnosti

- Celočíselná hodnota poskytovaná sítí, udávající míru preference pro převedení provozu
- Doručována prostřednictvím standardizovaných frameworků politik (ANDSF, politika UE)
- Ovlivňuje autonomní rozhodnutí UE o výběru přístupové sítě
- Spolupracuje s Indikátorem možnosti převedení provozu pro detailní řízení na úrovni jednotlivých toků
- Podporuje dynamické směrování na základě aktuálních podmínek zatížení sítě
- Umožňuje koexistenci s uživatelskými preferencemi a pravidly na straně zařízení

## Související pojmy

- [ANDSF – Access Network Discovery and Selection Function](/mobilnisite/slovnik/andsf/)

## Definující specifikace

- **TS 23.402** (Rel-19) — EPC for Non-3GPP Access (PMIP)
- **TS 24.302** (Rel-19) — Access to EPC via non-3GPP networks; Stage 3
- **TS 24.312** (Rel-19) — ANDSF Management Objects Specification
- **TS 25.300** (Rel-19) — UTRA Radio Interface Enhancements Overview
- **TS 36.300** (Rel-19) — E-UTRAN Radio Interface Protocol Architecture Overview

---

📖 **Anglický originál a plná specifikace:** [OPI na 3GPP Explorer](https://3gpp-explorer.com/glossary/opi/)
