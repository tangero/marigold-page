---
slug: "imb"
url: "/mobilnisite/slovnik/imb/"
type: "slovnik"
title: "IMB – Integrated Mobile Broadcast"
date: 2025-01-01
abbr: "IMB"
fullName: "Integrated Mobile Broadcast"
category: "Services"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/imb/"
summary: "Integrated Mobile Broadcast (IMB) je technologie 3GPP pro poskytování vysílacího obsahu (jako TV nebo rádio) prostřednictvím pozemních rádiových přístupových sítí UMTS. Efektivně využívá buňkový kmito"
---

IMB je technologie 3GPP, která využívá buňkové sítě UMTS k efektivnímu multicast vysílání vysílacího obsahu (např. TV nebo rádia) k mnoha uživatelům současně a integruje tyto služby do stávající mobilní infrastruktury.

## Popis

Integrated Mobile Broadcast (IMB) je standard 3GPP definovaný primárně pro sítě UMTS (3G), který umožňuje poskytování vysílacích a multicast služeb prostřednictvím stávající buňkové rádiové přístupové sítě. IMB využívá rádiovou technologii WCDMA a kmitočtový rozsah přidělený UMTS k přenosu vysílacího obsahu k více uživatelům současně, podobně jako tradiční vysílání, ale integrované do infrastruktury mobilního operátora. Systém je navržen pro práci s UMTS Terrestrial Radio Access Network (UTRAN), kde lze konfigurovat vyhrazené vysílací nosné nebo sdílené nosné pro přenos vysílacích dat. Klíčové specifikace pokrývají aspekty fyzické vrstvy (TS 25.102, TS 25.105), protokoly rádiového rozhraní (TS 25.221-224) a procedury vyšších vrstev (TS 25.304, TS 25.331).

IMB funguje tak, že na nosné UTRA zřídí vysílací režim. Síť nakonfiguruje vysílací kanál (jako je Secondary Common Control Physical Channel, S-CCPCH) pro přenos datového proudu vysílání. Uživatelé v oblasti vysílací služby se mohou naladit na tento kanál bez individuálních vyhrazených spojení a přijímat stejný obsah současně. To je efektivní pro oblíbené živé události nebo TV kanály. Z pohledu síťové architektury IMB zahrnuje Broadcast Multicast Service Center ([BM-SC](/mobilnisite/slovnik/bm-sc/)) pro poskytování služeb, prvky jádra sítě pro směrování vysílacích dat a uzly UTRAN (RNC a Node B) nakonfigurované pro podporu vysílacích přenosových režimů. Řízení rádiových zdrojů zahrnuje řízení výkonu optimalizované pro vysílání (konstantní nebo upravené na základě požadavků na pokrytí) a specifické modulační a kódovací schémata pro robustní příjem.

IMB podporuje jak vyhrazené vysílací nosné, kde je celá nosná přidělena výhradně pro vysílací služby, tak smíšené nosné, kde se vysílací a unicast služby dělí o stejnou nosnou pomocí různých časových slotů nebo kódů. Tato flexibilita umožňuje operátorům vyvážit využití kmitočtového rozsahu mezi vysíláním a konvenčními hlasovými/datovými službami. Technologie zahrnuje mechanismy pro oznámení služby, předplatné a zabezpečení (šifrování vysílacího obsahu). Jsou zohledněny i aspekty mobility; když se uživatel pohybuje, síť zajišťuje kontinuitu vysílací služby tím, že poskytuje informace o kmitočtech vysílacích nosných v sousedních buňkách. Integrace IMB do UMTS znamená, že využívá stávající plánování buněk, jádro sítě a systémy správy účastníků, což snižuje náklady a složitost nasazení vysílacích služeb ve srovnání s výstavbou samostatné vysílací sítě, jako je DVB-H.

## K čemu slouží

IMB byl vyvinut, aby řešil rostoucí poptávku po mobilních vysílacích službách, jako je mobilní TV a rádio, a zároveň efektivně využíval stávající síťovou infrastrukturu UMTS. Před IMB často vyžadovalo mobilní vysílání samostatné vyhrazené vysílací sítě (např. DVB-H, MediaFLO), což znamenalo dodatečný kmitočtový rozsah, infrastrukturu a zařízení, což vedlo k vysokým nákladům pro operátory a fragmentaci pro uživatele. Motivací pro IMB bylo umožnit buňkovým operátorům nabízet vysílací služby pomocí jejich již nasazených sítí a kmitočtového rozsahu UMTS a vytvořit tak integrovanou službovou nabídku.

Technologie řeší problém neefektivního unicast doručování oblíbeného obsahu. Streamování stejného TV kanálu k tisícům uživatelů individuálně spotřebovává nadměrné síťové zdroje. Multicast/vysílací režim IMB přenáší jeden datový proud k mnoha uživatelům, čímž šetří přenosovou kapacitu a snižuje zatížení sítě. Také umožňuje operátorům zpeněžit vysílací služby prostřednictvím stávajících modelů předplatného. Zavedený ve verzi 8 (Release 8) IMB navázal na dřívější multicast koncepty v 3GPP (jako [MBMS](/mobilnisite/slovnik/mbms/)), ale zaměřil se na integrovanější přístup v rámci UTRA. Cílem bylo poskytnout standardizovanou, efektivní metodu pro vysílací doručování, kterou by mohli implementovat operátoři UMTS bez zásadních přestaveb sítě, a podpořit tak přijetí mobilního vysílání jako životaschopné služby.

## Klíčové vlastnosti

- Vysílání přes UTRA využívající nosné WCDMA
- Podpora vyhrazených vysílacích nosných a smíšených nosných
- Efektivní multicast doručování k více uživatelům současně
- Integrace se stávající síťovou infrastrukturou UMTS (UTRAN, jádro)
- Mechanismy pro oznámení služby, předplatné a zabezpečení
- Podpora mobility pro kontinuitu vysílací služby napříč buňkami

## Související pojmy

- [MBMS – Multimedia Broadcast Multicast Service](/mobilnisite/slovnik/mbms/)

## Definující specifikace

- **TS 25.102** (Rel-19) — UTRA TDD RF Characteristics
- **TS 25.105** (Rel-19) — UTRA TDD Base Station RF Requirements
- **TS 25.142** (Rel-19) — UTRA TDD Base Station RF Test Methods
- **TS 25.221** (Rel-19) — UTRA TDD Physical Layer Specification
- **TS 25.222** (Rel-19) — UTRA TDD Multiplexing & Channel Coding
- **TS 25.223** (Rel-19) — UTRA Physical Layer TDD Spreading & Modulation
- **TS 25.224** (Rel-19) — UTRA TDD Physical Layer Procedures
- **TS 25.304** (Rel-19) — UTRA Idle Mode Procedures Specification
- **TS 25.331** (Rel-19) — UTRAN RRC Protocol Specification
- **TS 25.346** (Rel-19) — MBMS in UTRA Technical Specification
- **TS 25.402** (Rel-19) — UTRAN Synchronisation Mechanisms
- **TS 25.433** (Rel-19) — Node B Application Part (NBAP) Protocol

---

📖 **Anglický originál a plná specifikace:** [IMB na 3GPP Explorer](https://3gpp-explorer.com/glossary/imb/)
