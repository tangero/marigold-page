---
slug: "pdr"
url: "/mobilnisite/slovnik/pdr/"
type: "slovnik"
title: "PDR – Packet Detection Rule"
date: 2026-01-01
abbr: "PDR"
fullName: "Packet Detection Rule"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/pdr/"
summary: "Pravidlo pro detekci paketů (PDR) je základní pravidlový konstrukt ve funkci uživatelské roviny (UPF) 5G sítě a ve funkci pro detekci provozu (TDF) 4G/5G sítí. Definuje sadu kritérií pro shodu (např."
---

PDR je pravidlový konstrukt v UPF nebo TDF, který definuje kritéria pro shodu a akce k identifikaci a zpracování paketů uživatelské roviny pro směrování provozu a vynucování politik.

## Popis

Pravidlo pro detekci paketů (PDR) je ústředním prvkem zpracování paketů ve funkci uživatelské roviny ([UPF](/mobilnisite/slovnik/upf/)) jádra 5G sítě (5GC) dle 3GPP a používá se také ve funkci pro detekci provozu ([TDF](/mobilnisite/slovnik/tdf/)) 4G/5G sítí. Jde o pravidlo instalované funkcí pro správu relací ([SMF](/mobilnisite/slovnik/smf/)) prostřednictvím protokolu [PFCP](/mobilnisite/slovnik/pfcp/) (Packet Forwarding Control Protocol), které instruuje UPF, jak identifikovat a zacházet s konkrétními toky provozu uživatelské roviny. Každé PDR je v rámci PFCP relace jednoznačně identifikováno a obsahuje dvě hlavní části: sekci informací pro detekci paketů ([PDI](/mobilnisite/slovnik/pdi/)) a sadu přidružených akcí.

Informace pro detekci paketů (PDI) definují kritéria pro shodu používaná k identifikaci paketů náležících ke konkrétnímu toku. Může zahrnovat kombinaci polí, jako jsou zdrojová/cílová IP adresa, zdrojová/cílová čísla portů, identifikátor protokolu (např. TCP/[UDP](/mobilnisite/slovnik/udp/)), identifikátor toku QoS ([QFI](/mobilnisite/slovnik/qfi/)), instance sítě (identifikující virtuální síť), zdrojové/cílové rozhraní (např. přístupová strana, strana jádra) a identifikátory aplikací (z detekce a řízení aplikací). PDI poskytuje míru podrobnosti potřebnou k rozlišení různých služeb, uživatelů nebo síťových řezů. Když paket uživatelské roviny dorazí do UPF, je porovnáván se seznamem aktivních PDR podle jejich priority. První PDR, jehož PDI odpovídá paketu, je vybráno k provedení.

Jakmile paket odpovídá PDR, UPF provede uspořádaný seznam akcí přidružených k tomuto pravidlu. Mezi klíčové akce patří: přeposlání paketu na konkrétní cíl (např. do dalšího tunelu nebo k aplikační funkci), uložení paketu do bufferu (např. pro oznámení o downlink datech, když je UE v nečinném stavu), aplikace konkrétní politiky vynucení QoS (mapování na tok QoS, aplikování omezení přenosové rychlosti), spuštění hlášení o využití pro účtování a dynamická aktivace/deaktivace jiných PDR nebo pravidel pro vynucení QoS ([QER](/mobilnisite/slovnik/qer/)). Více PDR může být řetězově propojeno nebo vnořeno za účelem vytvoření složitých řetězců služebních funkcí, jako je směrování provozu přes firewall nebo optimalizátor videa před dosažením konečného cíle. Framework PDR poskytuje SMF výkonné programovatelné rozhraní pro řízení chování UPF na úrovni jednotlivých toků, což je zásadní pro podporu síťových řezů, edge computingu a diferencovaných služeb v 5G.

## K čemu slouží

PDR bylo vytvořeno, aby řešilo omezení statického, předem konfigurovaného filtrování a přeposílání paketů v předchozích mobilních jádrových sítích (jako GGSN ve 2G/3G). V těchto systémech bylo zacházení s provozem poměrně hrubé, často založené na APN nebo jednoduchých IP filtrech. Přechod na cloud-nativní, službami řízené jádro 5G si vyžádal mnohem flexibilnější, dynamičtější a detailnější mechanismus pro vynucování složitých politik definovaných řídicí rovinou (SMF). PDR jako součást protokolu PFCP toto umožňují oddělením řídicí logiky (v SMF) od vysokorychlostního zpracování paketů (v UPF), což umožňuje aplikaci politik specifických pro relaci v reálném čase.

Tato architektura řeší problém efektivní podpory různorodých případů užití 5G s výrazně odlišnými požadavky – od hromadného IoT vyžadujícího jednoduché přeposílání až po ultra-spolehlivé komunikace s nízkou latencí (URLLC) vyžadující přesné směrování provozu a garantovanou QoS. PDR umožňují síti dynamicky vytvářet a upravovat pravidla pro zacházení s provozem bez přerušení uživatelských relací. Například když uživatel zahájí videohovor, SMF může nainstalovat nové PDR k identifikaci tohoto konkrétního toku a aplikovat politiku QoS s vysokou prioritou. Tato úroveň dynamické kontroly nebyla v monolitické architektuře GGSN možná.

PDR jsou navíc zásadní pro umožnění síťových řezů a edge computingu. Různé síťové řezy vyžadují izolované přenosové cesty a politiky. PDR mohou porovnávat pakety na základě instance sítě (identifikátoru řezu) a směrovat je na příslušné virtualizované nebo fyzické zdroje. Pro edge computing mohou PDR směrovat provoz určený pro místní aplikační server přímo na lokální instanci uživatelské roviny na okraji sítě, čímž minimalizují latenci. Model PDR tedy poskytuje základní stavební kámen pro programovatelnou, agilní a na služby zaměřenou uživatelskou rovinu 5G.

## Klíčové vlastnosti

- Definuje kritéria pro shodu (PDI) pomocí IP/TCP/UDP hlaviček, rozhraní, QFI a identifikátoru aplikace
- Přiřazuje odpovídající pakety sadě uspořádaných akcí (přeposlat, uložit do bufferu, účtovat, vynutit QoS)
- Instalováno a upravováno dynamicky pro každou relaci funkcí SMF pomocí protokolu PFCP
- Podporuje řetězení a prioritu pro vytváření složitých řetězců služebních funkcí
- Umožňuje detailní detekci provozu pro vynucování politik a účtování
- Zásadní pro implementaci síťových řezů a lokálního výstupu (edge computing)

## Související pojmy

- [UPF – User Plane Function](/mobilnisite/slovnik/upf/)
- [PFCP – Packet Forwarding Control Protocol](/mobilnisite/slovnik/pfcp/)
- [QER – QoS Enforcement Rule](/mobilnisite/slovnik/qer/)
- [FAR](/mobilnisite/slovnik/far/)

## Definující specifikace

- **TS 23.501** (Rel-20) — 5G System Architecture Stage 2
- **TS 26.510** (Rel-19) — Media Delivery APIs for 5GMS and RTC Systems
- **TS 26.804** (Rel-19) — 5G Media Streaming Extensions Study
- **TS 29.244** (Rel-19) — PFCP Specification for Control/User Plane Separation

---

📖 **Anglický originál a plná specifikace:** [PDR na 3GPP Explorer](https://3gpp-explorer.com/glossary/pdr/)
