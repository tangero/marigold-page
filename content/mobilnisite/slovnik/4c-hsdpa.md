---
slug: "4c-hsdpa"
url: "/mobilnisite/slovnik/4c-hsdpa/"
type: "slovnik"
title: "4C-HSDPA – Four-Carrier High-Speed Downlink Packet Access"
date: 2025-01-01
abbr: "4C-HSDPA"
fullName: "Four-Carrier High-Speed Downlink Packet Access"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/4c-hsdpa/"
summary: "4C-HSDPA je vylepšení HSPA s více nosnými vlnami umožňující simultánní přenos na až čtyřech downlinkových nosných vlnách. Významně zvyšuje špičkové přenosové rychlosti a spektrální účinnost agregací v"
---

4C-HSDPA je vylepšení HSPA s více nosnými vlnami, které agreguje až čtyři downlinkové nosné vlny za účelem zvýšení špičkové přenosové rychlosti a spektrální účinnosti sítí UMTS/HSPA.

## Popis

4C-HSDPA je technologie agregace nosných vln v rámci vývojové linie [HSPA](/mobilnisite/slovnik/hspa/), která umožňuje uživatelskému zařízení (UE) přijímat data současně na až čtyřech downlinkových nosných vlnách, každé o šířce pásma 5 MHz. Technologie navazuje na dřívější implementace [HSDPA](/mobilnisite/slovnik/hsdpa/) s více nosnými vlnami ([DC-HSDPA](/mobilnisite/slovnik/dc-hsdpa/) a 3C-HSDPA) rozšířením schopnosti agregace nosných vln na čtyři, čímž efektivně vytváří virtuální šířku pásma až 20 MHz, pokud jsou všechny nosné vlny souvislé. Tato agregace probíhá na vrstvě řízení přístupu k médiu ([MAC](/mobilnisite/slovnik/mac/)), kde jsou data z více nosných vln plánována a koordinována pro maximalizaci propustnosti a spektrální účinnosti.

Z architektonického hlediska vyžaduje 4C-HSDPA vylepšení jak na straně Node B, tak UE. Node B musí podporovat simultánní přenos na více nosných vlnách s odpovídající alokací výkonu a koordinací plánování napříč nosnými vlnami. UE musí obsahovat více přijímacích řetězců schopných demodulovat signály z až čtyř nosných vln současně. Systém využívá plánování napříč nosnými vlnami, kde mohou být řídicí informace pro více nosných vln přenášeny na jediné primární nosné vlně, což snižuje režii řídicích kanálů. Každá nosná vlna si zachovává vlastní sadu fyzických kanálů včetně [HS-PDSCH](/mobilnisite/slovnik/hs-pdsch/) (High-Speed Physical Downlink Shared Channel) pro přenos dat a [HS-SCCH](/mobilnisite/slovnik/hs-scch/) (High-Speed Shared Control Channel) pro řídicí signalizaci, ačkoli řídicí informace mohou být konsolidovány.

Technologie funguje prostřednictvím procedur správy nosných vln, kdy síť nakonfiguruje UE sadou obslužných buněk, s jednou primární obslužnou buňkou a až třemi sekundárními obslužnými buňkami. UE monitoruje všechny nakonfigurované nosné vlny a přijímá povolení k plánování, která mohou alokovat prostředky napříč více nosnými vlnami ve stejném přenosovém časovém intervalu (TTI). Vrstva MAC na straně Node B i UE zpracovává distribuci a opětovné složení dat napříč nosnými vlnami, přičemž zachovává správné řazení a procesy [HARQ](/mobilnisite/slovnik/harq/) pro každou nosnou vlnu. Používají se pokročilé přijímací techniky včetně ekvalizace a potlačení interference, aby bylo možné zvládnout zvýšené nároky na zpracování signálu při příjmu z více nosných vln.

4C-HSDPA hraje klíčovou roli v sítích UMTS/HSPA tím, že poskytuje migrační cestu k vyšším přenosovým rychlostem bez nutnosti kompletní přestavby sítě na LTE. Umožňuje operátorům efektivněji využívat stávající spektrální zdroje agregací fragmentovaných alokací spektra. Technologie podporuje jak souvislou, tak nesouvislou agregaci nosných vln, což poskytuje flexibilitu při nasazování spektra. Z hlediska výkonu může 4C-HSDPA dosáhnout špičkových přenosových rychlostí až 168 Mbps za ideálních podmínek při použití modulace [64QAM](/mobilnisite/slovnik/64qam/) a technik MIMO, ačkoli praktická nasazení obvykle dosahují nižších rychlostí v závislosti na podmínkách kanálu a konfiguraci sítě.

## K čemu slouží

4C-HSDPA byl vyvinut, aby řešil rostoucí poptávku po vyšších přenosových rychlostech v sítích UMTS/HSPA v době, kdy se zrychlovalo přijímání chytrých telefonů a vzorce spotřeby dat se posouvaly směrem k aplikacím náročným na šířku pásma. Před jeho zavedením poskytovala 3C-HSDPA agregaci tří nosných vln se špičkovými rychlostmi až 63 Mbps, ale to se stávalo nedostatečným pro konkurenceschopnost s nastupujícími sítěmi LTE nabízejícími možnosti přes 100 Mbps. Technologie byla motivována potřebou prodloužit komerční životnost infrastruktury UMTS/HSPA a zároveň poskytnout hladkou migrační cestu k technologiím 4G.

Historicky se 4C-HSDPA objevil v období, kdy mnoho operátorů čelilo problému fragmentace spektra, kdy vlastnili více 5 MHz bloků v různých pásmech, které nemohly být efektivně využity pro technologie s širší šířkou pásma, jako je LTE. Umožněním agregace až čtyř nosných vln mohli operátoři kombinovat tyto fragmentované alokace a vytvářet efektivně širší kanály. To bylo obzvláště cenné na trzích, kde probíhalo přerozdělování spektra pro LTE pomalu kvůli regulačním nebo technickým omezením.

Technologie řešila několik klíčových omezení předchozích implementací HSPA. Jednonosné HSDPA bylo omezeno na špičkové rychlosti 14,4 Mbps, zatímco i 3C-HSDPA s MIMO dosahovalo pouze 63 Mbps. 4C-HSDPA zdvojnásobilo potenciální propustnost při zachování zpětné kompatibility se stávajícími UE. Rovněž řešilo obavy ohledně spektrální účinnosti tím, že umožnilo efektivnější využití dostupného spektra prostřednictvím pokročilých plánovacích algoritmů, které dokázaly vyvážit zátěž napříč více nosnými vlnami. Pro operátory to představovalo nákladově efektivní zvýšení kapacity bez nutnosti kompletní výměny sítě, což jim umožnilo odložit investice do LTE a zároveň uspokojovat rostoucí požadavky zákazníků na vyšší rychlosti.

## Klíčové vlastnosti

- Agregace až čtyř downlinkových nosných vln o šířce 5 MHz
- Teoretické špičkové přenosové rychlosti až 168 Mbps při použití 64QAM a MIMO
- Podpora jak souvislé, tak nesouvislé agregace nosných vln
- Plánování napříč nosnými vlnami pro snížení režie řídicích kanálů
- Zpětná kompatibilita s dřívějšími verzemi HSPA
- Vylepšené protokoly vrstvy MAC pro koordinaci více nosných vln

## Související pojmy

- [HSDPA – High Speed Downlink Packet Access](/mobilnisite/slovnik/hsdpa/)
- [DC-HSDPA – Dual Cell High Speed Downlink Packet Access](/mobilnisite/slovnik/dc-hsdpa/)

## Definující specifikace

- **TS 25.104** (Rel-19) — UTRA FDD Base Station RF Characteristics
- **TS 25.141** (Rel-19) — UTRA FDD Base Station RF Conformance Testing
- **TS 25.327** (Rel-19) — Multi-carrier HSDPA UE requirements

---

📖 **Anglický originál a plná specifikace:** [4C-HSDPA na 3GPP Explorer](https://3gpp-explorer.com/glossary/4c-hsdpa/)
