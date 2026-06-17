---
slug: "n-pdu"
url: "/mobilnisite/slovnik/n-pdu/"
type: "slovnik"
title: "N-PDU – Network Protocol Data Unit"
date: 2025-01-01
abbr: "N-PDU"
fullName: "Network Protocol Data Unit"
category: "Protocol"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/n-pdu/"
summary: "N-PDU (Network Protocol Data Unit) je paket nebo datová jednotka vyměňovaná mezi protějškovými entitami na síťové vrstvě (vrstva 3) v rámci protokolové architektury 3GPP. Obsahuje uživatelská data a i"
---

N-PDU je datová jednotka síťové vrstvy v systémech 3GPP, která obsahuje uživatelská data a hlavičku pro směrování v paketově orientovaných doménách, jako jsou GPRS a EPS.

## Popis

N-PDU (Network Protocol Data Unit) je klíčový koncept v paketově orientovaných síťových protokolech 3GPP, který představuje datový paket tak, jak jej vidí a zpracovává síťová vrstva (vrstva 3). Skládá se z hlavičky síťové vrstvy (obsahující řídicí informace, jako jsou adresy a identifikátory protokolů) a užitečného zatížení (payload), což jsou uživatelská data nebo datová jednotka služby (SDU) z vyšší vrstvy. V kontextu služby General Packet Radio Service ([GPRS](/mobilnisite/slovnik/gprs/)), paketově orientované domény UMTS a Evolved Packet System (EPS) je N-PDU základní jednotkou přenosu dat mezi uživatelským zařízením (UE) a sítí a uvnitř samotné core sítě.

Architektonicky je N-PDU vytvořen protokolem síťové vrstvy v odesílateli (např. Subnetwork Dependent Convergence Protocol (SNDCP) v GPRS nebo Packet Data Convergence Protocol (PDCP) v UMTS a LTE). Tento protokol zapouzdří IP paket (nebo jiné užitečné zatížení vrstvy 3) z UE a přidá potřebné hlavičky pro funkce jako komprese, šifrování a doručování ve správném pořadí. Toto N-PDU je pak předáno podlézající vrstvě datového spoje (např. [LLC](/mobilnisite/slovnik/llc/) v GPRS, RLC v UMTS/LTE) pro další zpracování a přenos přes rozhraní vzduchu.

Jak to funguje, zahrnuje vícevrstvý proces zapouzdření. Při přenosu dat v uplinku generuje IP zásobník UE IP paket. Vrstva GPRS SNDCP například komprimuje tuto IP hlavičku a volitelně i data, poté vytvoří SNDCP-PDU, což je v podstatě N-PDU pro síťovou vrstvu GPRS. Toto N-PDU je pak segmentováno do rámců Logical Link Control (LLC) pro spolehlivé doručení přes rozhraní Um/Gb. V core síti může Serving GPRS Support Node (SGSN) zpracovat N-PDU pro účely tunelování, zapouzdřit jej uvnitř GPRS Tunneling Protocol ([GTP](/mobilnisite/slovnik/gtp/)) PDU pro přenos k Gateway GPRS Support Node (GGSN). Jeho úlohou je poskytnout standardizovanou, na vrstvě nezávislou datovou jednotku, kterou mohou protokoly síťové vrstvy směrovat, spravovat a zabezpečovat napříč celým paketově orientovaným systémem.

## K čemu slouží

N-PDU existuje proto, aby poskytlo jasnou, standardizovanou abstrakci pro data na síťové vrstvě, oddělující problematiku přenosu uživatelských dat od podlézajících přenosových mechanismů. Řeší problém, jak efektivně a spolehlivě přenášet IP pakety proměnné délky (nebo jiné protokoly síťové vrstvy) přes specifické rádiové a core síťové protokoly definované 3GPP. Před standardizací paketových dat v mobilních sítích byly datové služby spojově orientované a neefektivní.

Vytvoření konceptu N-PDU bylo motivováno zavedením [GPRS](/mobilnisite/slovnik/gprs/), které vyžadovalo paketově orientovanou nadstavbu nad stávající spojově orientovanou sítí GSM. Poskytlo způsob, jak definovat datovou jednotku, která bude podléhat klíčovým funkcím síťové vrstvy, jako je komprese hlaviček (pro úsporu rádiových prostředků), šifrování (pro zabezpečení) a segmentace (pro přizpůsobení rámcům nižší vrstvy). Řeší omezení plynoucí z chápání uživatelských dat jako transparentního bitového toku tím, že umožňuje síťové vrstvě inteligentně zpracovávat a spravovat datovou jednotku pro optimální výkon a spolehlivost na heterogenní cestě od UE k externí paketové datové síti.

## Klíčové vlastnosti

- Představuje datovou jednotku vrstvy 3 v paketových protokolech 3GPP
- Obsahuje hlavičku síťové vrstvy pro směrování a řídicí informace
- Užitečné zatížení je typicky IP paket nebo SDU vyšší vrstvy
- Podléhá funkcím síťové vrstvy, jako je komprese hlaviček a šifrování
- Je zapouzdřováno a rozbalováno protokoly jako SNDCP a PDCP
- Základní jednotka pro tunelování v core síti (např. v rámci GTP)

## Související pojmy

- [GTP – GPRS Tunnelling Protocols](/mobilnisite/slovnik/gtp/)

## Definující specifikace

- **TS 23.060** (Rel-19) — GPRS Service Description Stage 2
- **TS 24.007** (Rel-19) — GSM Um Interface Layer 3 Architecture
- **TS 25.413** (Rel-19) — Radio Access Network Application Part (RANAP)

---

📖 **Anglický originál a plná specifikace:** [N-PDU na 3GPP Explorer](https://3gpp-explorer.com/glossary/n-pdu/)
