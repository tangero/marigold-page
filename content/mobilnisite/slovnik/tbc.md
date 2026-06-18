---
slug: "tbc"
url: "/mobilnisite/slovnik/tbc/"
type: "slovnik"
title: "TBC – Token Bucket Counter"
date: 2025-01-01
abbr: "TBC"
fullName: "Token Bucket Counter"
category: "QoS"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/tbc/"
summary: "Algoritmus pro kontrolu (policing) provozu používaný k vynucování parametrů kvality služby (QoS) měřením a řízením přenosové rychlosti a velikosti shluku dat toku. Konceptuálně využívá tokeny, které j"
---

TBC je algoritmus pro kontrolu (policing) provozu, který využívá token bucket k měření a řízení přenosové rychlosti a velikosti shluku dat, čímž zajišťuje, že provoz odpovídá definovaným parametrům kvality služby (QoS).

## Popis

Token Bucket Counter (TBC) je základní algoritmus implementovaný v síťových uzlech, jako je Policy and Charging Enforcement Function ([PCEF](/mobilnisite/slovnik/pcef/)) nebo uživatelské zařízení (UE), pro kontrolu (policing) toků provozu vůči přihlášenému profilu QoS. Funguje na základě konceptuálního modelu zahrnujícího 'bucket' (sběrnici), který obsahuje 'tokeny'. Tokeny jsou generovány a přidávány do bucketu konstantní rychlostí, známou jako Committed Information Rate ([CIR](/mobilnisite/slovnik/cir/)). Samotný bucket má maximální kapacitu, která definuje Committed Burst Size ([CBS](/mobilnisite/slovnik/cbs/)). Když dorazí paket, TBC zkontroluje, zda je v bucketu dostatek tokenů odpovídajících velikosti paketu. Pokud jsou tokeny k dispozici, jsou spotřebovány (odebrány z bucketu) a paket je považován za konformní a je přeposlán. Pokud tokenů není dostatek, paket je považován za nekonformní, což spustí politickou akci, jako je označení (marking), tvarování (shaping) nebo zahození (dropping).

Stav algoritmu je definován aktuálním počtem tokenů a časem poslední aktualizace. Aby se předešlo neustálým výpočtům generování tokenů, počet se typicky aktualizuje líně (lazy) – pouze když je třeba vyhodnotit paket. Vzorec přepočítá počet tokenů na základě uplynulého času od posledního paketu a rychlosti generování tokenů, s horním limitem na maximální velikost bucketu. Tento návrh efektivně vynucuje jak dlouhodobou průměrnou rychlost (prostřednictvím rychlosti generování tokenů), tak limit pro krátkodobé shluky (bursts) (prostřednictvím velikosti bucketu). TBC je klíčovou součástí mechanismů pro vynucování Guaranteed Bit Rate ([GBR](/mobilnisite/slovnik/gbr/)) a Maximum Bit Rate ([MBR](/mobilnisite/slovnik/mbr/)) specifikovaných v 3GPP pro přenašeče EPS a 5GS.

V rámci architektury 3GPP jsou parametry TBC odvozeny z pravidel QoS poskytovaných funkcí Policy and Charging Rules Function ([PCRF](/mobilnisite/slovnik/pcrf/)) nebo Policy Control Function ([PCF](/mobilnisite/slovnik/pcf/)). Tyto parametry se uplatňují na každý QoS tok (5GS) nebo přenašeč EPS. Vynucovací bod používá TBC ke sledování provozu v uplinku a/nebo downlinku, čímž zajišťuje, že provoz v uživatelské rovině nepřekročí smluvně dohodnuté limity. To je zásadní pro ochranu síťových zdrojů, spravedlivé využití mezi účastníky a umožnění vrstvených služeb. Specifikace podrobně popisují, jak jsou tyto parametry token bucket mapovány z deskriptorů QoS, jako je 5G QoS Identifier ([5QI](/mobilnisite/slovnik/5qi/)) a Allocation and Retention Priority (ARP).

## K čemu slouží

Token Bucket Counter byl standardizován, aby poskytl standardizovanou, předvídatelnou a efektivní metodu pro kontrolu (policing) provozu v paketově přepínaných mobilních sítích. Jak se sítě vyvíjely od okruhově přepínané hlasové služby k IP multimediálním službám, řízení datového provozu se stalo nezbytným pro prevenci zahlcení sítě, zaručení výkonu prémiových služeb a implementaci účtovacích modelů založených na objemu a rychlosti dat. Jednoduché statické omezovače rychlosti nedokázaly efektivně zvládnout trhanou (bursty) povahu IP provozu.

Algoritmus TBC řeší tento problém oddělením řízení průměrné rychlosti od tolerance k trhanosti (burstiness). To byl významný pokrok oproti jednodušším schématům typu leaky bucket nebo čistého omezování rychlosti. Umožňuje aplikacím s proměnnou přenosovou rychlostí (jako je streamování videa) přenášet shluky paketů, pokud si 'nashromáždily' tokeny, čímž vyhlazuje provoz a zlepšuje využití přenosové cesty, a zároveň stále vynucuje dlouhodobé smluvní limity. Jeho zavedení v éře R99/UMTS položilo technický základ pro sofistikované rámce QoS a řízení politik (policy control), které jsou ústřední pro sítě 4G a 5G, a umožnilo diferenciaci služeb mezi hlasem, videem a daty s best-effort přístupem.

## Klíčové vlastnosti

- Vynucuje Committed Information Rate (CIR) a Committed Burst Size (CBS)
- Umožňuje řízenou trhanost (burstiness) v mezích velikosti token bucketu
- Používá se pro kontrolu (policing) provozu s Guaranteed Bit Rate (GBR) a Maximum Bit Rate (MBR)
- Nedílná součást vynucování Policy and Charging Control (PCC)
- Funguje na úrovni QoS toku nebo přenašeče EPS
- Používá se v uplink i downlink směru

## Související pojmy

- [5QI – 5G QoS Identifier](/mobilnisite/slovnik/5qi/)

## Definující specifikace

- **TS 23.107** (Rel-19) — UMTS QoS Framework
- **TS 23.207** (Rel-19) — End-to-End QoS Framework for GPRS

---

📖 **Anglický originál a plná specifikace:** [TBC na 3GPP Explorer](https://3gpp-explorer.com/glossary/tbc/)
