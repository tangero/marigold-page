---
slug: "dr"
url: "/mobilnisite/slovnik/dr/"
type: "slovnik"
title: "DR – Designated Router"
date: 2025-01-01
abbr: "DR"
fullName: "Designated Router"
category: "Core Network"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/dr/"
summary: "Logická funkce routeru v architektuře Edge Computingu (MEC) 5G Core Network. Je zodpovědná za efektivní směrování provozu mezi uživatelským zařízením (UE) a místními aplikačními servery hostovanými na"
---

DR je logická funkce routeru v Edge Computingu 5G, která efektivně směruje provoz mezi uživatelským zařízením (User Equipment) a místními aplikačními servery na okraji sítě.

## Popis

Designated Router (DR) je funkční entita definovaná v architektuře 5G Core Network pro podporu Edge Computingu, konkrétně detailně popsaná v rámci pro umožnění okrajových aplikací. Nachází se v cestě uživatelské roviny, typicky spolusídlená s nebo poblíž funkce uživatelské roviny ([UPF](/mobilnisite/slovnik/upf/)), která obsluhuje konkrétní lokální oblast nebo datovou síť. Primární role DR spočívá v tom, že funguje jako inteligentní směrovací kotva pro provoz určený do aplikací nasazených na okraji sítě nebo pocházející z nich.

Operačně, když je relace UE navázána s okrajovým aplikačním serverem ([EAS](/mobilnisite/slovnik/eas/)), 5G core síť (prostřednictvím [SMF](/mobilnisite/slovnik/smf/)) nakonfiguruje UPF a přidružený DR příslušnými pravidly pro směrování provozu. DR zkoumá IP pakety proudící z UE. Na základě cílové IP adresy a potenciálně dalších filtrů paketů rozhoduje, zda je provoz určen pro místní EAS, nebo má být směrován do centrálního internetu či cloudu. Pro provoz určený místnímu EAS provádí DR nezbytné funkce překladu síťových adres ([NAT](/mobilnisite/slovnik/nat/)) nebo IP směrování, aby nasměroval pakety do místní datové sítě, kde se EAS nachází, čímž se vyhne zbytečné latenci způsobené směrováním do centrálního datového centra.

Architektonicky je DR klíčovou součástí pro realizaci efektivního odlehčení provozu na okraji sítě. Funguje ve spolupráci s funkcí správy relací (SMF), která poskytuje zásady směrování, a s funkcí vystavení sítě ([NEF](/mobilnisite/slovnik/nef/)) nebo klientem/servery Edge Enabler, které usnadňují objevování aplikací. DR může implementovat funkce jako zachování IP adresy UE pro EAS, duplikaci provozu pro analytiku a integraci s konceptem místní datové sítě ([LADN](/mobilnisite/slovnik/ladn/)). Jeho nasazení je zásadní pro služby s nízkou latencí, jako je průmyslový IoT, rozšířená realita a komunikace vozidla se vším (V2X), protože zajišťuje, že uživatelský provoz využívá nejpřímější cestu k nejbližší instanci aplikace, čímž minimalizuje dobu odezvy a přetížení přenosové trasy.

## K čemu slouží

Designated Router byl zaveden k řešení výzev spojených se směrováním provozu, které jsou vlastní distribuovaným architekturám Edge Computingu v rámci 5G. Jak se aplikace přesouvaly z centralizovaných cloudů na okraj sítě za účelem snížení latence, byl potřebný mechanismus, který by zajistil efektivní a dynamické nasměrování provozu UE na správnou místní instanci aplikace bez složité konfigurace na straně klienta nebo neefektivního směrování přes centrální bod a zpět.

Předchozí architektury mobilních sítí postrádaly standardizovanou, síťově řízenou funkci pro detailní směrování místního provozu na okraji sítě. Řešení byla často závislá na dodavateli nebo spoléhala na externí SDN kontroléry. DR, standardizovaný počínaje 3GPP Release 16, poskytuje nativní, protokolově agnostickou směrovací funkci v rámci uživatelské roviny 3GPP. Řeší problém transparentního připojení UE k optimálnímu okrajovému aplikačnímu serveru na základě síťových politik a polohy UE. To umožňuje případy užití vyžadující ultra-spolehlivou komunikaci s nízkou latencí (URLLC) a vysokou přenosovou rychlost díky vytváření efektivních lokalizovaných datových cest. Jeho vznik byl motivován posunem průmyslu směrem k multi-access edge computingu ([MEC](/mobilnisite/slovnik/mec/)) a potřebou, aby 5G core nativně podporoval směrování s ohledem na kontext aplikace, což je zásadní pro naplnění výkonnostních slibů 5G.

## Klíčové vlastnosti

- Směruje provoz UE na místní okrajové aplikační servery (EAS)
- Provádí IP směrování a potenciálně funkce NAT na okraji sítě
- Funguje pod kontrolou zásad směrování provozu poskytovaných SMF
- Umožňuje komunikační cesty s nízkou latencí pro okrajové aplikace
- Podporuje integraci s koncepty místní datové sítě (LADN)
- Usnadňuje efektivní odlehčení provozu na okraji sítě a úspory v přenosové trase

## Související pojmy

- [UPF – User Plane Function](/mobilnisite/slovnik/upf/)
- [SMF – Service Management Function](/mobilnisite/slovnik/smf/)
- [EAS – Enterprise Application Server](/mobilnisite/slovnik/eas/)
- [LADN – Local Area Data Network](/mobilnisite/slovnik/ladn/)

## Definující specifikace

- **TS 29.561** (Rel-19) — 5G Interworking with External Data Networks

---

📖 **Anglický originál a plná specifikace:** [DR na 3GPP Explorer](https://3gpp-explorer.com/glossary/dr/)
