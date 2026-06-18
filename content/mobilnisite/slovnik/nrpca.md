---
slug: "nrpca"
url: "/mobilnisite/slovnik/nrpca/"
type: "slovnik"
title: "NRP – Network Requested PDP Context Activation"
date: 2025-01-01
abbr: "NRP"
fullName: "Network Requested PDP Context Activation"
category: "Core Network"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/nrpca/"
summary: "Procedura v sítích GPRS a UMTS, při které síťové jádro (GGSN) zahajuje navázání datové relace (PDP kontextu) směrem k mobilnímu zařízení. To umožňuje síti doručit data do zařízení nebo je přimět k nav"
---

NRP je procedura v sítích GPRS/UMTS, při které síťové jádro zahajuje navázání datové relace směrem k mobilnímu zařízení, aby umožnilo push služby nebo stále připojené IP spojení.

## Popis

Network Requested [PDP](/mobilnisite/slovnik/pdp/) Context Activation (NRP) je procedura jádra sítě definovaná pro paketově orientovanou doménu 2.5G ([GPRS](/mobilnisite/slovnik/gprs/)) a 3G (UMTS). PDP (Packet Data Protocol) kontext je logická asociace mezi mobilním zařízením ([MS](/mobilnisite/slovnik/ms/)/UE) a sítí, která definuje parametry datové relace, jako je IP adresa, QoS profil a obsluhující GGSN. Normálně PDP kontext aktivuje mobilní zařízení. NRP tento tok obrací a umožňuje síti, konkrétně Gateway GPRS Support Node (GGSN), spustit aktivaci PDP kontextu směrem k zařízení, které je připojeno k GPRS, ale nemusí mít aktivní datovou relaci.

Procedura funguje následovně: Když externí Packet Data Network ([PDN](/mobilnisite/slovnik/pdn/)), jako je internet nebo podniková síť, má data určená pro mobilního účastníka, pošle datové pakety k účastníkovu GGSN. Pokud GGSN nenajde pro tohoto účastníka aktivní PDP kontext (tj. zařízení nemá navázanou IP relaci), může zahájit proceduru NRP. GGSN odešle zprávu s žádostí o aktivaci PDP kontextu k [SGSN](/mobilnisite/slovnik/sgsn/), které účastníka aktuálně obsluhuje. Tato žádost obsahuje klíčové parametry jako Access Point Name ([APN](/mobilnisite/slovnik/apn/)), požadovanou QoS a přidělenou PDP adresu (IP adresu). SGSN následně lokalizuje mobilní zařízení a přepošle mu žádost o aktivaci konkrétního PDP kontextu.

Po přijetí této síťově iniciované žádosti mobilní zařízení typicky odpoví zahájením standardní procedury aktivace PDP kontextu iniciované mobilem směrem k síti, s využitím parametrů poskytnutých GGSN. Tím se obousměrně naváže datová relace. Klíčovými síťovými komponentami jsou GGSN (která žádost iniciuje), SGSN (která žádost směruje do správné obsluhované oblasti a spravuje kontext mobility) a [HLR](/mobilnisite/slovnik/hlr/) (Home Location Register) nebo v pozdějších architekturách [HSS](/mobilnisite/slovnik/hss/), které může GGSN dotazovat, aby zjistilo aktuální obsluhující SGSN pro účastníka, pokud není známo.

Role NRP je klíčová pro umožnění mobilními terminovaných paketových datových služeb. Umožňuje síti „probudit“ zařízení k přijetí dat, podporuje zážitek „stále připojeno“, kdy je zařízení dosažitelné bez nutnosti udržovat konstantní datový bearer, čímž šetří baterii zařízení a rádiové zdroje. Je základním mechanismem pro push služby, kdy server potřebuje zahájit komunikaci s mobilním klientem. Procedura zajišťuje, že potřebný datový bearer s odpovídající QoS je navázán právě včas pro doručení příchozích dat, což optimalizuje využití síťových zdrojů ve srovnání s udržováním trvalých relací pro všechna připojená zařízení.

## K čemu slouží

NRP bylo vytvořeno, aby vyřešilo základní omezení raných sítí GPRS: neschopnost sítě zahájit datovou relaci k mobilnímu zařízení. Ve standardním modelu mohl PDP kontext aktivovat pouze mobilní terminál. To stačilo pro služby iniciované klientem, jako je prohlížení webu, ale znemožňovalo služby iniciované serverem, jako je přijetí notifikace e-mailu, instantní zprávy nebo mobilní terminovaného VoIP hovoru. Bez NRP by bylo zařízení dosažitelné pro data pouze tehdy, pokud by mělo předem navázaný a udržovaný aktivní PDP kontext, což bylo neefektivní z hlediska baterie a síťových zdrojů.

Primární problém, který NRP řeší, je umožnění push a mobilními terminovaných datových služeb způsobem šetrným k prostředkům. Umožňuje síti spustit nastavení datové cesty na vyžádání, když pro účastníka dorazí data. To bylo klíčovým prvkem pro uživatelský zážitek neustálého připojení, který byl zamýšlen pro datové služby 2.5G a 3G. Motivací bylo učinit paketově orientované sítě stejně přijímající vůči příchozím relacím, jako byly sítě s přepojováním okruhů pro hlasové hovory, a tím podpořit novou generaci interaktivních a push služeb.

Historicky, před NRP, byla řešení neefektivní, například periodické dotazování serverů zařízeními nebo udržování stále aktivních kontextů. NRP, zavedené ve 3GPP Release 6 jako součást vylepšeného IP Multimedia Subsystem (IMS) a obecných požadavků na datové služby, poskytlo standardizované, síťově efektivní řešení. Vyřešilo omezení modelu pouze iniciovaného mobilem definováním přesné signalizace mezi GGSN, SGSN a UE. Tento vývoj byl klíčový pro úspěch služeb jako push e-mail BlackBerry, Presence služby a později bohatých IMS aplikací, což učinilo z mobilního zařízení skutečný obousměrný IP koncový bod.

## Klíčové vlastnosti

- Umožňuje GGSN zahájit navázání PDP kontextu směrem k mobilnímu zařízení GPRS/UMTS
- Spouští aktivaci při příchodu dat pro účastníka bez aktivní relace
- Využívá standardní signalizaci GTP-C mezi GGSN a SGSN pro žádost
- Umožňuje síti navrhnout parametry relace (APN, QoS, IP adresu)
- Klíčové pro push služby (e-mail, zasílání zpráv) a mobilními terminované datové relace
- Podporuje efektivitu zdrojů navazováním bearerů na vyžádání namísto udržování stále aktivních relací

## Související pojmy

- [SGSN – Serving GPRS Support Node](/mobilnisite/slovnik/sgsn/)
- [APN – Access Point Name](/mobilnisite/slovnik/apn/)
- [GTP – GPRS Tunnelling Protocols](/mobilnisite/slovnik/gtp/)

## Definující specifikace

- **TR 23.976** (Rel-19) — Push Service Requirements Analysis

---

📖 **Anglický originál a plná specifikace:** [NRP na 3GPP Explorer](https://3gpp-explorer.com/glossary/nrpca/)
