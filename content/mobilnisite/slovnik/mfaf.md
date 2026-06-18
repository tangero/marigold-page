---
slug: "mfaf"
url: "/mobilnisite/slovnik/mfaf/"
type: "slovnik"
title: "MFAF – Messaging Framework Adaptor Function"
date: 2026-01-01
abbr: "MFAF"
fullName: "Messaging Framework Adaptor Function"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/mfaf/"
summary: "Funkce 5G páteřní sítě zavedená ve verzi 17 (Release 17), která poskytuje standardizovaný rámec pro doručování zpráv a jejich vystavení poskytovatelům aplikací třetích stran. Umožňuje efektivní, bezpe"
---

MFAF (Funkce adaptoru zasílacího rámce) je funkce 5G páteřní sítě, která poskytuje standardizovaný rámec pro zabezpečené, zásadami řízené doručování zpráv a jejich vystavení poskytovatelům aplikací třetích stran.

## Popis

Messaging Framework Adaptor Function (MFAF, Funkce adaptoru zasílacího rámce) je komponenta architektury založené na službách ([SBA](/mobilnisite/slovnik/sba/)) v rámci 5G páteřní sítě (5GC), definovaná jako síťová funkce ([NF](/mobilnisite/slovnik/nf/)). Funguje jako centrální adaptor a expoziční bod pro služby zasílání zpráv. Z architektonického hlediska rozhraní MFAF komunikuje s ostatními funkcemi páteřní sítě, jako je Network Exposure Function ([NEF](/mobilnisite/slovnik/nef/)) a Unified Data Management ([UDM](/mobilnisite/slovnik/udm/)), aby bezpečně vystavila možnosti zasílání zpráv. Také se připojuje k externím aplikačním serverům a starším systémům zasílání zpráv, jako je IP Multimedia Subsystem (IMS) pro SMS-over-IP (SMS-IP) nebo jiné aplikační servery zasílání zpráv. Její primární role spočívá v abstrahování základních síťových složitostí a poskytování jednotného, standardizovaného [API](/mobilnisite/slovnik/api/) rámce pro doručování zpráv, umožňujícího různé modely zasílání včetně komunikace osoba-osoba (P2P), aplikace-osoba ([A2P](/mobilnisite/slovnik/a2p/)) a konverzačního zasílání zpráv (např. [RCS](/mobilnisite/slovnik/rcs/)).

Operačně MFAF zajišťuje směrování zpráv, vymáhání zásad a provádění servisní logiky. Když je zpráva odeslána od externího poskytovatele aplikací, MFAF ověří a autorizuje požadavek přes NEF, použije příslušné zásady (např. kontrola spamu, pravidla účtování) a určí optimální doručovací cestu. Může komunikovat s UDM pro získání dat o účastníkovi a informací o směrování. Pro doručení na UE může zprávu předat příslušnému [SMSC](/mobilnisite/slovnik/smsc/), IMS nebo přímo Access and Mobility Management Function (AMF) pro NAS transport, v závislosti na typu zprávy a konfiguraci sítě. Podporuje funkce jako doručovací zprávy, stanovení priority zpráv a hromadné odesílání zpráv.

Vnitřní architektura MFAF zahrnuje rozhraní založená na službách (SBI), jako je Nmfaf pro severní expozici, a rozhraní k ostatním NF. Mezi klíčové komponenty patří Adaptační logika, která překládá mezi externími API formáty a vnitřními síťovými protokoly; funkce pro vymáhání zásad (Policy Enforcement Function), která aplikuje pravidla definovaná operátorem; a funkce spouštějící účtování (Charging Trigger Function), která generuje záznamy o účtovaných datech. Její zavedení představuje posun od monolitických, izolovaných systémů zasílání zpráv (jako tradiční SMSC) k flexibilnímu, cloud-nativnímu rámci, který může snadno integrovat nové služby zasílání zpráv a API, podporující inovace v ekosystému zasílání zpráv 5G.

## K čemu slouží

MFAF byla vytvořena jako odpověď na vyvíjející se prostředí zasílání zpráv v éře 5G, kde tradiční SMS a MMS koexistují s pokročilými komunikačními službami (RCS) a novými službami aplikace-osoba. Před jejím zavedením bylo vystavení služeb zasílání zpráv třetím stranám často realizováno pomocí proprietárních bran nebo omezených API, což vedlo k fragmentaci, bezpečnostním problémům a neefektivnímu využívání síťových zdrojů. MFAF poskytuje standardizovaný, bezpečný a škálovatelný rámec uvnitř 5G páteře s cílem sjednotit tyto přístupové metody.

Její vývoj byl motivován potřebou podporovat nové obchodní modely, jako je A2P zasílání zpráv pro ověřování podniků, marketing a oznámení, které vyžadují robustní kontrolu zásad, účtování a kvalitu služby. Dále, jak se sítě vyvíjejí směrem k cloud-nativním, na službách založeným architekturám, byla nutná specializovaná funkce pro správu složitosti spolupráce mezi staršími systémy zasílání zpráv a novými rozhraními 5G založenými na službách. MFAF řeší tyto problémy tím, že nabízí centralizovaný adaptor, který zjednodušuje integraci pro poskytovatele aplikací a zároveň dává síťovým operátorům detailní kontrolu nad provozem zasílání zpráv, bezpečností a zpoplatněním.

## Klíčové vlastnosti

- Standardizovaná rozhraní založená na službách (např. Nmfaf) pro severní expozici API poskytovatelům aplikací
- Vymáhání zásad pro provoz zasílání zpráv, včetně kontroly spamu, omezení rychlosti a správy QoS
- Podpora více typů zasílání zpráv: SMS, MMS, RCS a konverzačního zasílání
- Integrace s funkcemi 5GC, jako je NEF pro bezpečnou expozici a UDM pro data účastníků
- Funkce účtování s generováním záznamů o účtovaných datech pro fakturaci
- Možnosti spolupráce se staršími systémy zasílání zpráv (např. SMSC) a sítěmi IMS

## Související pojmy

- [NEF – Network Exposure Function](/mobilnisite/slovnik/nef/)
- [UDM – Unified Data Management](/mobilnisite/slovnik/udm/)

## Definující specifikace

- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TS 23.700** (Rel-20) — XR Services Application Enablement Layer
- **TS 29.517** (Rel-19) — 5G AF Event Exposure Service Stage 3
- **TS 29.520** (Rel-19) — 5G Network Data Analytics Services Stage 3
- **TS 29.552** (Rel-19) — 5G Network Data Analytics Signalling Flows
- **TS 29.564** (Rel-19) — Nupf Service Based Interface Protocol
- **TS 29.575** (Rel-19) — 5G Analytics Data Repository Services Stage 3
- **TS 29.576** (Rel-19) — 5G Messaging Framework Adaptor Services Stage 3
- **TS 29.591** (Rel-19) — 5G NEF Southbound Services Stage 3
- **TS 29.889** (Rel-19) — Study on UPF data collection for AI/ML

---

📖 **Anglický originál a plná specifikace:** [MFAF na 3GPP Explorer](https://3gpp-explorer.com/glossary/mfaf/)
