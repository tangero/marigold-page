---
slug: "udd"
url: "/mobilnisite/slovnik/udd/"
type: "slovnik"
title: "UDD – Unconstrained Delay Data"
date: 2025-01-01
abbr: "UDD"
fullName: "Unconstrained Delay Data"
category: "QoS"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/udd/"
summary: "Třída QoS pro datový provoz bez specifických požadavků na zpoždění, jako jsou stahování na pozadí nebo e-mail. Umožňuje síti oportunisticky plánovat přenos, optimalizovat využití zdrojů bez garance la"
---

UDD je třída QoS pro datový provoz v reálném čase, jako jsou stahování na pozadí, která nemá specifické požadavky na zpoždění a umožňuje síti oportunisticky plánovat přenosy pro optimalizaci využití zdrojů.

## Popis

Unconstrained Delay Data (UDD) je standardizovaná třída provozu Quality of Service (QoS) definovaná v architektuře 3GPP, určená speciálně pro paketové datové služby v reálném čase. Je charakterizována absencí přísných požadavků na zpoždění nebo jeho variaci (jitter). Primární architektonické umístění UDD je v rámci QoS rámce paketové domény ([PS](/mobilnisite/slovnik/ps/) domain), řízené parametry v kontextu Packet Data Protocol ([PDP](/mobilnisite/slovnik/pdp/)) nebo, v novějších verzích, v QoS Flow v 5G systému. Síť zpracovává provoz UDD na bázi best-effort, což znamená, že zdroje jsou alokovány až po uspokojení potřeb vyšších prioritních, na zpoždění citlivých tříd provozu (jako konverzační nebo streamovací).

Operačně, když uživatelské zařízení (UE) aktivuje PDP kontext nebo zřizuje [PDU](/mobilnisite/slovnik/pdu/) Session pro službu UDD, žádá o QoS profil specifikující třídu provozu UDD. Klíčové parametry QoS spojené s UDD zahrnují Traffic Handling Priority (THP), která může být použita k rozlišení mezi různými toky UDD, a Allocation/Retention Priority ([ARP](/mobilnisite/slovnik/arp/)). Guaranteed Bit Rate ([GBR](/mobilnisite/slovnik/gbr/)) se na UDD nevztahuje; místo toho může být spojena s Maximum Bit Rate ([MBR](/mobilnisite/slovnik/mbr/)) pro omezení její spotřeby šířky pásma. Uzly jádra sítě, jako [SGSN](/mobilnisite/slovnik/sgsn/) v 3G/4G nebo [SMF](/mobilnisite/slovnik/smf/) v 5G, spolu s rádiovou přístupovou sítí (RAN), používají tyto parametry pro řízení přístupu a plánování.

Plánovač RAN hraje klíčovou roli v řízení provozu UDD. Používá algoritmy, které upřednostňují rádiové zdroje pro přenosy v reálném čase. Pakety UDD jsou typicky buffrovány a přenášeny v obdobích nižšího síťového zatížení nebo když rádiové podmínky jsou příznivé pro vysoce efektivní modulační a kódovací schémata. Toto oportunistické plánování maximalizuje celkovou spektrální efektivitu a kapacitu sítě. UDD je zásadní pro služby jako stahování souborů, aktualizace softwaru a synchronizace e-mailů, kde přesný čas doručení paketu není pro uživatelský zážitek kritický, ale spolehlivé konečné doručení je vyžadováno.

V architektuře služeb end-to-end tvoří UDD základ pro přístup k internetu. Interaguje s dalšími QoS mechanismy jako DiffServ v transportní síti. Architektura policy and charging control (PCC), zahrnující PCRF (Policy and Charging Rules Function) nebo PCF (Policy Control Function), může definovat pravidla, která mapují aplikační provoz do třídy UDD, což operátorům umožňuje řídit síťové zdroje a aplikovat odpovídající tarifní politiky pro best-effort datové služby.

## K čemu slouží

UDD bylo vytvořeno pro formální kategorizaci a správu drtivé většiny internetového datového provozu, který nevyžaduje výkon v reálném čase. Před standardizovanými třídami QoS bylo se všemi daty zacházeno jednotně jako s best-effort, což bylo neefektivní při mísení s nově vznikajícími službami v reálném čase jako Voice over IP (VoIP). Zavedení odlišných tříd provozu v 3GPP R99 umožnilo operátorům implementovat inteligentní správu provozu.

Primární problém, který UDD řeší, je efektivní využití vzácných a drahých rádiových zdrojů. Díky jasné identifikaci provozu, který snáší zpoždění, může síťový plánovač tento provoz upozadit ve prospěch konverzačního nebo streamovacího provozu, čímž zajistí dobrou kvalitu zážitku pro aplikace citlivé na latenci. Toto zabraňuje tomu, aby přenosy dat na pozadí degradovaly hlasové nebo videohovory. Dále poskytuje standardizovaný rámec pro diferenciaci služeb, což operátorům umožňuje nabízet stupňované datové tarify a implementovat politiky spravedlivého používání.

Jeho vytvoření bylo motivováno potřebou vyvinout mobilní sítě z primárně okruhově přepínaných hlasových systémů na integrované paketově přepínané sítě schopné podporovat širokou škálu datových služeb. UDD představuje 'pozadí' ve víceúrovňovém QoS modelu, což je zásadní pro škálovatelný a ziskový mobilní broadband. Řeší omezení jednoduché best-effort sítě tím, že umožňuje předvídatelnou degradaci služeb pro nekritický provoz při přetížení, namísto nepředvídatelné degradace pro veškerý provoz.

## Klíčové vlastnosti

- Definována jako non-GBR (Non-Guaranteed Bit Rate) třída QoS.
- Žádné specifické požadavky na přenosové zpoždění nebo jeho variaci (jitter).
- Typicky spojena s parametrem Traffic Handling Priority (THP) pro plánování uvnitř třídy.
- Využívá Allocation and Retention Priority (ARP) pro řízení přístupu při přetížení zdrojů.
- Oportunisticky plánována RAN pro maximalizaci spektrální efektivity.
- Základní třída pro best-effort přístup k internetu a datům aplikací na pozadí.

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions

---

📖 **Anglický originál a plná specifikace:** [UDD na 3GPP Explorer](https://3gpp-explorer.com/glossary/udd/)
