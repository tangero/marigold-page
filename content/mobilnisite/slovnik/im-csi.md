---
slug: "im-csi"
url: "/mobilnisite/slovnik/im-csi/"
type: "slovnik"
title: "IM-CSI – IP Multimedia CAMEL Subscription Information"
date: 2025-01-01
abbr: "IM-CSI"
fullName: "IP Multimedia CAMEL Subscription Information"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/im-csi/"
summary: "IM-CSI je prvek profilu předplatného CAMEL, který umožňuje síti aplikovat řízení služeb založené na CAMEL na relace IP Multimedia Subsystem (IMS). Operátorům umožňuje nabízet inteligentní, předplacené"
---

IM-CSI je prvek profilu předplatného CAMEL, který umožňuje řízení služeb založené na CAMEL pro relace IP Multimedia Subsystem (IMS), což operátorům poskytuje možnost nabízet inteligentní a předplacené služby pro multimediální hovory v IMS.

## Popis

IP Multimedia [CAMEL](/mobilnisite/slovnik/camel/) Subscription Information (IM-CSI) je klíčový datový prvek uložený v Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)) jako součást profilu IMS služeb uživatele. Obsahuje potřebné spouštěče aplikační logiky CAMEL a adresy (konkrétně adresu gsmSCF) vyžadované pro vyvolání služeb založených na CAMEL Application Part ([CAP](/mobilnisite/slovnik/cap/)) pro relace IMS. Když uživatel zahájí nebo přijme relaci IMS (jako je VoIP hovor nebo videoschůzka), Serving-Call Session Control Function (S-CSCF) načte profil uživatele z HSS. Pokud je IM-CSI přítomen, S-CSCF použije tuto informaci k navázání dialogu s určeným CAMEL Service Environment ([CSE](/mobilnisite/slovnik/cse/)) nebo Service Control Function (gsmSCF). To umožňuje gsmSCF vykonávat kontrolu nad relací IMS, podobně jako CAMEL řídí hovory v přepojování okruhů, což umožňuje provádění aplikační logiky v reálném čase.

Architektura zahrnuje HSS, S-CSCF a gsmSCF. Data IM-CSI zahrnují Service Key, adresu gsmSCF a specifické Detection Points ([DP](/mobilnisite/slovnik/dp/)), které definují, kdy má S-CSCF kontaktovat gsmSCF – typicky při událostech zřízení, změny nebo ukončení relace. Při dosažení nakonfigurovaného DP odešle S-CSCF operaci CAP InitialDP nebo ekvivalentní operaci do gsmSCF. gsmSCF pak může dát S-CSCF pokyny, jak s relací dále postupovat, například aplikovat rady k účtování, přesměrovat hovor nebo komunikovat s dalšími síťovými prvky pro kombinování služeb. Tento mechanismus umožňuje, aby jádro IMS bylo řízeno externí, operátorem definovanou aplikační logikou.

Jeho role spočívá v usnadnění migrace a integrace služeb inteligentní sítě ([IN](/mobilnisite/slovnik/in/)) z domény přepojování okruhů do paketové domény IMS. Zajišťuje, že operátoři mohou využít stávající investice do CAMEL a prostředí pro tvorbu služeb k nabízení pokročilých IMS služeb v reálném čase, jako je předplacená multimediální telefonie, bezplatná čísla pro videohovory nebo přizpůsobené směrování hovorů na základě stavu přítomnosti v IMS. IM-CSI tak funguje jako most, který umožňuje robustnímu paradigmatu řízení služeb CAMEL ovládat multimediální relace založené na SIP, a poskytuje tak konzistentní uživatelský zážitek ze služeb napříč síťovými doménami.

## K čemu slouží

IM-CSI byl vytvořen, aby řešil potřebu řízení služeb inteligentní sítě uvnitř IP Multimedia Subsystem (IMS), který byl představen ve 3GPP Release 5. Před IMS byl [CAMEL](/mobilnisite/slovnik/camel/) rozsáhle používán v sítích 2G a 3G s přepojováním okruhů k poskytování specifických, přidaných služeb operátorů, jako je předplacené volání, překlad čísel nebo filtrování hovorů. Jak se sítě vyvíjely směrem k architekturám all-IP s IMS pro multimediální služby, vznikla jasná potřeba rozšířit tento ověřený rámec řízení služeb do nové domény relací založených na SIP.

Hlavní problém, který řeší, je umožnění bezproblémové kontinuity služeb a stejných funkcí. Bez IM-CSI by byli operátoři nuceni vyvíjet zcela nové, oddělené mechanismy řízení služeb pro IMS, což by vedlo k duplikaci úsilí a potenciálně ke vzniku mezer ve službách. IM-CSI umožňuje opětovné použití stávajících platforem služeb CAMEL (gsmSCF) a aplikační logiky, čímž chrání investice a urychluje nasazení IMS služeb. Konkrétně řeší výzvu aplikace řízení IMS relací v reálném čase, řízeného událostmi, které jsou inherentně složitější než jednoduché hlasové hovory a zahrnují více mediálních komponent a kodeků.

Historicky bylo jeho zavedení v Release 99 základním krokem pro umožnění služeb IMS, motivovaným snahou o hladký přechod z inteligentních sítí s přepojováním okruhů na paketové multimediální služby. Odstranilo omezení starších specifikací CAMEL, které byly navrženy pouze pro řízení hovorů s přepojováním okruhů a SMS, definováním spouštěčů a procedur potřebných pro řízení SIP relací. Tím bylo zajištěno, že operátoři mohli nabízet známé inteligentní služby (např. předplacené) pro nové hlasové, video a messagingové služby založené na IMS, což podpořilo adopci IMS a jeho komerční životaschopnost.

## Klíčové vlastnosti

- Umožňuje řízení služeb CAMEL pro relace IMS založené na SIP
- Ukládá se jako součást profilu IMS předplatného uživatele v HSS
- Obsahuje adresu gsmSCF a service key pro vyvolání služby
- Definuje Detection Points pro události IMS relací (např. zřízení relace)
- Umožňuje gsmSCF řídit směrování relace, účtování a ukončení
- Podporuje integraci starších služeb IN s novými generacemi sítí IMS

## Související pojmy

- [CAMEL – Customised Applications for Mobile network Enhanced Logic](/mobilnisite/slovnik/camel/)
- [IMS – IP Multimedia Subsystem](/mobilnisite/slovnik/ims/)
- [HSS – Home Subscriber Server](/mobilnisite/slovnik/hss/)

## Definující specifikace

- **TS 23.218** (Rel-19) — IMS Call Model Specification
- **TS 23.278** (Rel-19) — CAMEL for IMS Stage 2 Specification

---

📖 **Anglický originál a plná specifikace:** [IM-CSI na 3GPP Explorer](https://3gpp-explorer.com/glossary/im-csi/)
