---
slug: "mme-rn"
url: "/mobilnisite/slovnik/mme-rn/"
type: "slovnik"
title: "MME-RN – MME serving the RN"
date: 2025-01-01
abbr: "MME-RN"
fullName: "MME serving the RN"
category: "Core Network"
segment: "Security"
canonical: "https://3gpp-explorer.com/glossary/mme-rn/"
summary: "Specifická funkční role Mobility Management Entity (MME) v sítích LTE, která poskytuje služby řídicí roviny Relay Node (RN). MME-RN zpracovává jedinečné procedury autentizace, mobility a správy relací"
---

MME-RN je specifická funkční role Mobility Management Entity v sítích LTE, která zajišťuje jedinečné procedury autentizace, mobility a správy relací pro Relay Node.

## Popis

[MME](/mobilnisite/slovnik/mme/) obsluhující Relay Node (MME-RN) je specializovaná logická funkce uvnitř standardní MME, která spravuje řídicí rovinu pro Relay Node v síti LTE-Advanced. Relay Node je nízkovýkonný eNodeB, který rozšiřuje pokrytí a kapacitu bezdrátovým připojením k donor eNodeB (DeNB) přes rozhraní Un, namísto použití kabelové přenosové sítě. MME-RN je zodpovědná za správu [RN](/mobilnisite/slovnik/rn/), jako by šlo o specializovaný typ User Equipment (UE) pro jeho vlastní signalizaci řídicí roviny, zatímco RN současně funguje jako základnová stanice pro skutečná UE.

Z architektonického hlediska se MME-RN nachází v jádru sítě a připojuje se k donor [eNB](/mobilnisite/slovnik/enb/) přes standardní rozhraní [S1-MME](/mobilnisite/slovnik/s1-mme/). Procedury se však liší. Když se RN zapne, provede proceduru Attach, ale ta je vůči MME-RN považována za 'RN Attach'. MME-RN autentizuje RN pomocí přihlašovacích údajů uložených v [HSS](/mobilnisite/slovnik/hss/), naváže EPS bezpečnostní kontext a spravuje jeho mobilitu, protože se může potenciálně přesouvat mezi různými donor eNB. Klíčovou roli hraje MME-RN také při nastavování datové roviny pro RN. Účastní se vytváření jednoho nebo více vyhrazených bearerů (často [GTP](/mobilnisite/slovnik/gtp/) tunelů) mezi RN a Serving Gateway ([S-GW](/mobilnisite/slovnik/s-gw/)) pro vlastní provoz RN ([OAM](/mobilnisite/slovnik/oam/)) a, což je důležitější, pro agregovaný uživatelský provoz všech UE připojených k danému RN.

Jak to funguje, zahrnuje vrstvenou konektivitu. MME-RN vidí RN jako jedinou entitu s vlastním International Mobile Subscriber Identity (IMSI). Uživatelská rovina pro UE za RN je agregována přes toto připojení RN. MME-RN nespravuje jednotlivá UE připojená k RN; tuto funkci vykonává samostatná MME (MME-UE). Mezi hlavní zodpovědnosti MME-RN patří RN-specifická autentizace a autorizace, zpracování handoverů RN mezi donor eNB, správa PDN připojení RN pro jeho přenosovou síť a podpora RN-specifických bezpečnostních procedur definovaných v TS 33.401. Její role je zásadní pro bezproblémovou integraci bezdrátových přenosových uzlů do EPC, což jim umožňuje být samokonfigurovatelnými a spravovatelnými entitami v síti operátora.

## K čemu slouží

Funkce MME-RN byla vytvořena, aby řešila specifické výzvy řídicí roviny spojené s funkcí LTE Relay Node, standardizovanou v 3GPP Release 10. Relay Node byly navrženy jako nákladově efektivní řešení pro rychlé rozšíření pokrytí, zejména v oblastech, kde je nasazení optické přenosové sítě obtížné nebo drahé. Přenosový uzel však není prostý opakovač; jde o plnohodnotný eNodeB, který vyžaduje vlastní správu, autentizaci a připojení k jádru sítě.

Problém spočíval v tom, že standardní procedury MME navržené pro ruční UE byly nedostačující. RN má dvojí povahu: je infrastrukturou z pohledu UE, která obsluhuje, ale je také 'mobilním terminálem' z pohledu sítě, ke které se připojuje (donor eNB). Účelem definice role MME-RN bylo přizpůsobit jádro sítě tak, aby tuto dualitu rozpoznalo a zvládlo. Řeší potřebu zabezpečeného, autentizovaného vstupu infrastrukturního uzlu do sítě, což je klíčové pro prevenci neoprávněných základnových stanic.

Dále umožňuje efektivní správu mobility a relací pro RN. Jako bezdrátový uzel může RN potřebovat předat spojení mezi různými donor eNB (např. u mobilních přenosových uzlů pro vlaky). MME-RN tyto procedury zpracovává. Také vytváří složitou architekturu bearerů, která umožňuje RN mít vlastní řídicí provoz a zároveň směrovat agregovaný uživatelský provoz všech připojených UE přes zabezpečený tunel. Bez MME-RN by jádro sítě nemělo standardizovaný způsob, jak tyto bezdrátové přenosové body spravovat, zabezpečovat a integrovat, což by omezilo flexibilitu jejich nasazení a provozní robustnost.

## Klíčové vlastnosti

- Zpracovává RN-specifické procedury Attach a Detach
- Spravuje autentizaci a navázání bezpečnostního kontextu pro Relay Node
- Řídí nastavení a modifikaci PDN připojení pro přenosovou síť RN
- Podporuje procedury handoveru RN mezi různými donor eNB
- Spolupracuje s HSS na údajích o účastníkovi RN a autentizaci
- Odlišná od MME-UE, která spravuje koncová uživatelská zařízení za RN

## Související pojmy

- [S1-MME – S1 Control Plane Interface to the Mobility Management Entity](/mobilnisite/slovnik/s1-mme/)

## Definující specifikace

- **TS 33.401** (Rel-19) — EPS Security Architecture
- **TS 33.816** (Rel-11) — Security Analysis for LTE Relay Nodes

---

📖 **Anglický originál a plná specifikace:** [MME-RN na 3GPP Explorer](https://3gpp-explorer.com/glossary/mme-rn/)
