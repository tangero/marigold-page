---
slug: "pcn"
url: "/mobilnisite/slovnik/pcn/"
type: "slovnik"
title: "PCN – Packet-switched Core Network Node"
date: 2025-01-01
abbr: "PCN"
fullName: "Packet-switched Core Network Node"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/pcn/"
summary: "Obecný termín 3GPP zahrnující všechny uzly jádra sítě zodpovědné za paketově orientované datové služby, včetně SGSN, GGSN, S-GW, P-GW a TDF. Poskytuje jednotný referenční bod pro funkce politik, účtov"
---

PCN je obecný termín 3GPP pro všechny paketově orientované uzly jádra sítě (packet-switched core network nodes), jako jsou SGSN a P-GW, poskytující jednotný referenční bod pro politiky (policy), účtování (charging) a správu napříč sítěmi 2G, 3G a 4G.

## Popis

Paketově orientovaný uzel jádra sítě (Packet-switched Core Network Node – PCN) je souhrnný termín definovaný ve specifikacích 3GPP, zejména v kontextu rámců pro politiky, účtování a správu. Odkazuje na jakýkoli uzel v paketově orientované doméně jádra sítě, který zpracovává uživatelský datový provoz a podléhá řízení politik a pravidlům účtování. Koncept PCN abstrahuje konkrétní typy uzlů napříč různými generacemi systémů 3GPP ([GPRS](/mobilnisite/slovnik/gprs/), EPS, 5GS) do společné kategorie pro účely řízení politik a účtování ([PCC](/mobilnisite/slovnik/pcc/)) a správy sítě.

Z architektonického hlediska jsou uzly PCN hlavními prvky uživatelské roviny. V sítích 2G/3G GPRS zahrnuje PCN Serving GPRS Support Node ([SGSN](/mobilnisite/slovnik/sgsn/)) a Gateway GPRS Support Node (GGSN). SGSN je zodpovědný za správu relací, správu mobility a směrování datových paketů do/z rádiové přístupové sítě (RAN). GGSN slouží jako kotvící bod k externím paketovým datovým sítím (např. internet). Ve 4G Evolved Packet System (EPS) zahrnuje PCN Serving Gateway ([S-GW](/mobilnisite/slovnik/s-gw/)) a Packet Data Network Gateway ([P-GW](/mobilnisite/slovnik/p-gw/)). S-GW je lokální kotva mobility, zatímco P-GW poskytuje rozhraní k externím sítím a provádí hlubokou inspekci paketů (DPI), vynucování politik a účtování. Traffic Detection Function ([TDF](/mobilnisite/slovnik/tdf/)), volitelný uzel, je také považován za PCN; provádí detekci aplikací a hlášení, což slouží jako vstup pro [PCRF](/mobilnisite/slovnik/pcrf/) pro rozhodování o politikách.

Jak to funguje: Uživatelské datové pakety procházejí jedním nebo více uzly PCN. Každý uzel PCN uplatňuje politiky diktované funkcí Policy and Charging Rules Function (PCRF) přes rozhraní Gx (pro P-GW/GGSN) nebo jiné referenční body. Tyto politiky řídí kvalitu služby (QoS), tvarování provozu a účtovací akce. Pro online účtování PCN komunikuje s Online Charging System ([OCS](/mobilnisite/slovnik/ocs/)) přes rozhraní Gy. Pro offline účtování generuje záznamy o účtování dat (CDR) a odesílá je funkci Charging Data Function (CDF) přes rozhraní Ga. PCN je tedy bodem vynucení politik (PEP) a funkcí spouštění účtování (CTF). Jeho úlohou je provádět rozhodnutí učiněná řídicími entitami politik v řídicí rovině.

Klíčové komponenty v uzlu PCN zahrnují funkce zpracování uživatelské roviny (přeposílání paketů, tunelování pomocí GTP-U), funkce řídicí roviny (GTP-C pro správu relací) a integrovanou funkci vynucení politik a účtování (PCEF). PCEF je kritická komponenta, která inspektuje pakety, uplatňuje QoS označení (např. nastavení hodnot DSCP), propouští/zastavuje datové toky a měří využití pro účtování. Význam PCN spočívá v tom, že poskytuje konzistentní bod pro aplikaci obchodní logiky (politik) a monetizace (účtování) napříč vyvíjejícími se síťovými architekturami, bez ohledu na konkrétní název uzlu nebo detaily protokolu.

## K čemu slouží

Termín PCN byl zaveden za účelem vytvoření jednotného, na technologii nezávislého referenčního bodu pro uzly zapojené do doručování paketově orientovaných dat ve standardech 3GPP. Jak se sítě vyvíjely z GPRS přes EPS k 5GS, konkrétní názvy uzlů a některé funkce se změnily (SGSN/GGSN na S-GW/P-GW). Nicméně základní potřeba aplikovat politiky a účtování na datovou cestu zůstala konstantní. Abstrakce PCN řeší problém nutnosti definovat rozhraní pro politiky a účtování zvlášť pro každou generaci uzlů jádra, čímž zjednodušuje specifikaci a implementaci.

Historicky, před formalizací konceptu PCN, musely specifikace politik a účtování explicitně vypisovat všechny příslušné uzly (SGSN, GGSN atd.). To se stalo těžkopádným s každou novou generací sítě a zaváděním nových typů uzlů, jako je TDF. Termín PCN, zavedený přibližně od Release 8 se zdokonalením PCC architektury, poskytuje kategorii odolnou vůči budoucím změnám. Umožňuje definovat PCC rámec (PCRF, PCEF) pomocí logických funkcí (např. 'PCN musí vynucovat QoS') namísto konkrétních fyzických entit.

Tato abstrakce řeší omezení těsného propojení řízení politik s konkrétními implementacemi uzlů. Umožňuje flexibilnější, službami orientovanou architekturu, kde bod rozhodování o politikách (PCRF) může vydávat příkazy jakémukoli uzlu, který plní roli PCN, ať už se jedná o legacy GGSN nebo cloud-nativní P-GW. Také usnadňuje sdílení sítě a interoperabilitu mezi více dodavateli definováním společných požadavků na chování pro všechny paketové brány jádra sítě.

## Klíčové vlastnosti

- Abstrahuje konkrétní paketové uzly jádra sítě (SGSN, GGSN, S-GW, P-GW, TDF) pod jedinou funkční kategorii
- Slouží jako bod vynucení politik a účtování (PCEF) pro provoz v uživatelské rovině
- Generuje záznamy o účtování dat (CDR) pro offline fakturaci
- Komunikuje s Online Charging System (OCS) pro řízení kreditu v reálném čase
- Vynucuje QoS politiky (propouštění/zastavování toku, omezení šířky pásma, označování priority) podle pokynů PCRF
- Kotví uživatelské relace a spravuje datové přenosy/tunely (GTP)

## Definující specifikace

- **TS 32.251** (Rel-19) — PS Domain Charging Management
- **TS 32.298** (Rel-19) — Charging Data Record (CDR) Parameter Specification

---

📖 **Anglický originál a plná specifikace:** [PCN na 3GPP Explorer](https://3gpp-explorer.com/glossary/pcn/)
