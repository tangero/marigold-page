---
slug: "nmp"
url: "/mobilnisite/slovnik/nmp/"
type: "slovnik"
title: "NMP – Number of Missing PDCP SDUs"
date: 2025-01-01
abbr: "NMP"
fullName: "Number of Missing PDCP SDUs"
category: "Radio Access Network"
segment: "Radio Access Network"
canonical: "https://3gpp-explorer.com/glossary/nmp/"
summary: "Výkonnostní metrika vrstvy PDCP, která počítá počet servisních datových jednotek (SDUs), které nebyly úspěšně doručeny ve správném pořadí. Je klíčovým ukazatelem ztráty paketů a kvality rádiového spoj"
---

NMP je výkonnostní metrika vrstvy PDCP, která počítá počet chybějících servisních datových jednotek (Service Data Units) a slouží jako indikátor ztráty paketů a kvality rádiového spoje pro účely odstraňování problémů a monitorování QoS.

## Popis

Počet chybějících [PDCP](/mobilnisite/slovnik/pdcp/) SDUs (NMP) je kritický čítač vedený vrstvou Packet Data Convergence Protocol (PDCP) jak v uživatelském zařízení (UE), tak v základnové stanici (eNodeB v LTE, gNB v NR). Konkrétně sleduje servisní datové jednotky (SDUs), které jsou na přijímající PDCP entitě detekovány jako chybějící z očekávané sekvence. [SDU](/mobilnisite/slovnik/sdu/) je považováno za 'chybějící', když přijímač obdrží PDCP protokolovou datovou jednotku ([PDU](/mobilnisite/slovnik/pdu/)) s pořadovým číslem ([SN](/mobilnisite/slovnik/sn/)), které je vyšší než další očekávané pořadové číslo v sekvenci, což indikuje mezeru v pořadí. Tato mezera značí, že jedna nebo více SDUs byla ztracena, pravděpodobně kvůli chybám v nižších vrstvách ([RLC](/mobilnisite/slovnik/rlc/), [MAC](/mobilnisite/slovnik/mac/), [PHY](/mobilnisite/slovnik/phy/)) nebo na rádiovém rozhraní.

Čítač NMP se zvýší o jedničku za každou detekovanou chybějící SDU. Jeho fungování je úzce spojeno s funkcí doručování a přeřazování do pořadí (in-order delivery and reordering) v PDCP. Pro každý přenosový kanál (bearer) přijímající PDCP entita (ať už v uplinku na straně gNB nebo v downlinku na straně UE) udržuje přijímací okno a proměnnou 'Next_PDCP_RX_SN'. Když dorazí PDU s pořadovým číslem (X) větším než 'Next_PDCP_RX_SN', znamená to, že všechny SDUs s pořadovými čísly mezi 'Next_PDCP_RX_SN' a X-1 chybějí. Čítač NMP je odpovídajícím způsobem zvýšen. Tyto chybějící SDUs mohou být obnoveny, pokud nižší vrstva RLC pracuje v potvrzovaném režimu (Acknowledged Mode, [AM](/mobilnisite/slovnik/am/)) a úspěšně vyžádá opakovaný přenos, ale metrika PDCP NMP zachycuje počáteční událost ztráty ze své perspektivy.

NMP je zásadní měřítko výkonnosti pro operátora sítě. Často je hlášena prostřednictvím čítačů správy výkonnosti (PM counters) z RAN do systému řízení. Vysoká nebo rychle rostoucí hodnota NMP na konkrétní buňce nebo pro konkrétní UE je silným indikátorem špatných rádiových podmínek, přetížení nebo problémů s hardwarem. Přímo koreluje s uživatelsky vnímanou ztrátou paketů a zhoršením služeb, jako je VoIP nebo video streamování. Tato metrika se používá v algoritmech pro monitorování rádiového spoje, spouštění předání spojení (handover triggering, pokud jsou ztráty trvalé) a úpravy QoS. V pokročilých implementacích může sloužit jako vstup pro modely strojového učení pro prediktivní detekci výpadků buněk nebo optimalizaci sítě.

## K čemu slouží

Metrika NMP byla zavedena, aby poskytla jasné, standardizované měřítko ztráty paketů na vrstvě PDCP, což je poslední protokolová vrstva před předáním dat uživatelské roviny do jádra sítě (nebo aplikaci v UE). Před její explicitní definicí bylo možné ztrátu paketů pouze nepřímo odvozovat z metrik nižších vrstev (jako jsou RLC retransmise nebo HARQ NACKy) nebo z metrik aplikací na koncích spojení. Tato nepřímá měření mohla být nejednoznačná; například vysoký počet RLC retransmisí nutně neznamená, že pakety byly nakonec ztraceny, pokud byly obnoveny.

NMP řeší problém přesného kvantifikování ztráty servisních dat, která je patrná koncovým uživatelským aplikacím. Poskytuje přímý, jednoznačný počet datových jednotek, které nedorazily ve správném pořadí na PDCP přijímač. To je klíčové pro monitorování smluv o úrovni služeb (SLAs), zejména pro služby s přísnými požadavky na ztrátovost, jako je hlas (VoLTE) nebo hraní v reálném čase. Umožňuje operátorům přesně určit, zda ke ztrátě paketů dochází v rádiovém segmentu (vysoké NMP) nebo jinde na cestě mezi koncovými body.

Její vytvoření bylo motivováno potřebou podrobnějších a na vrstvu specifických ukazatelů výkonnosti v LTE a přechodem k samoorganizujícím se sítím (SON). Jak se sítě stávaly složitějšími a automatizovanějšími, přesné metriky jako NMP se staly nezbytnými pro automatizovanou analýzu příčin problémů a optimalizaci. Sledováním trendů NMP může síť automaticky spouštět nápravné akce, jako je úprava parametrů předání spojení, změna sklonu antény nebo dokonce označení potenciálního výpadku lokalizace buňky, čímž se zlepšuje celková spolehlivost sítě a uživatelský zážitek.

## Klíčové vlastnosti

- Přímé měření ztráty PDCP SDU na přijímači
- Založeno na mezerách v pořadových číslech (Sequence Number) PDCP
- Hlášeno jako čítač správy výkonnosti (PM counter) ze strany RAN
- Klíčový ukazatel kvality rádiového spoje a přetížení
- Používá se pro monitorování QoS a reportování SLA
- Slouží jako vstup pro algoritmy optimalizace sítě a SON

## Související pojmy

- [PDCP – Packet Data Convergence Protocol](/mobilnisite/slovnik/pdcp/)
- [RLC – Radio Link Control](/mobilnisite/slovnik/rlc/)
- [QoS – Quality of Service](/mobilnisite/slovnik/qos/)

## Definující specifikace

- **TS 36.323** (Rel-19) — PDCP Protocol Specification

---

📖 **Anglický originál a plná specifikace:** [NMP na 3GPP Explorer](https://3gpp-explorer.com/glossary/nmp/)
