---
slug: "upn"
url: "/mobilnisite/slovnik/upn/"
type: "slovnik"
title: "UPN – Update Notification"
date: 2025-01-01
abbr: "UPN"
fullName: "Update Notification"
category: "Protocol"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/upn/"
summary: "Zpráva GTPv2-C používaná na rozhraní S5/S8 mezi SGW a PGW k informování PGW o změnách stavu nebo konfigurace SGW. Zajišťuje kontinuitu relace a správnou správu přenosových kanálů během událostí mobili"
---

UPN je zpráva GTPv2-C používaná na rozhraní S5/S8 k informování PGW o změnách stavu SGW, čímž zajišťuje kontinuitu relace a správnou správu přenosových kanálů během mobility nebo aktualizací sítě.

## Popis

Update Notification (UPN) je specifická zpráva GTPv2-C ([GPRS](/mobilnisite/slovnik/gprs/) Tunneling Protocol verze 2 pro řídicí rovinu) definovaná v 3GPP TS 29.275. Funguje na rozhraní S5 (uvnitř stejné [PLMN](/mobilnisite/slovnik/plmn/)) nebo S8 (mezi PLMN) spojujícím Serving Gateway ([SGW](/mobilnisite/slovnik/sgw/)) a Packet Data Network Gateway ([PGW](/mobilnisite/slovnik/pgw/)) v Evolved Packet Core (EPC). Primární funkcí zprávy UPN je informovat PGW o změně stavu nebo konfigurace SGW, která je relevantní pro správu aktivních [PDN](/mobilnisite/slovnik/pdn/) připojení a EPS přenosových kanálů. Jedná se o klíčový mechanismus pro udržení kontinuity relace a zajištění, že PGW má přesný pohled na topologii sítě pro směrování paketů.

Když dojde k události vyžadující aktualizaci, jako je změna SGW během předávání mezi SGW, SGV sestaví a odešle zprávu UPN do PGW. Tato zpráva obsahuje informační prvky (IEs), které specifikují povahu změny. Mezi klíčové IEs patří Cause, který udává důvod notifikace (např. změna SGW z důvodu mobility UE), a [F-TEID](/mobilnisite/slovnik/f-teid/) (Fully Qualified Tunnel Endpoint Identifier) SGW pro řídicí rovinu, který musí PGW použít pro následující signalizaci. Po přijetí UPN PGW zpracuje informace, aktualizuje svůj interní kontext pro dotčené UE a odpoví zprávou Update Notification Acknowledge ([UPA](/mobilnisite/slovnik/upa/)). Toto potvrzení zajišťuje synchronizaci obou uzlů.

Mechanismus UPN je nedílnou součástí správy mobility, zejména ve scénářích jako Tracking Area Update ([TAU](/mobilnisite/slovnik/tau/)) nebo předávání, která spouštějí přemístění SGW. Umožňuje PGW, které je kotvou pro IP relaci UE, být neprodleně informováno o novém SGW obsluhujícím UE. To umožňuje PGW správně směrovat downlink datové pakety přes nový GTP-U tunel zřízený s novým SGW. Dále může být UPN použito pro jiné administrativní nebo obnovovací účely, jako je notifikace PGW o restartu SGW, což umožňuje PGW provést příslušné akce, jako je opětovné zřízení přenosových kanálů nebo vyčištění zastaralých kontextů.

## K čemu slouží

Update Notification (UPN) byl zaveden k řešení potřeby spolehlivé synchronizace stavu mezi SGW a PGW v architektuře EPC. Před jeho formální definicí byly mechanismy pro informování kotvící brány (PGW) o změnách v mezilehlé bráně (SGW) méně standardizované nebo spoléhaly na implicitní spouštěče, což mohlo vést k přerušení relace nebo suboptimálnímu směrování během událostí mobility. Vytvoření vyhrazené zprávy GTPv2-C poskytlo jasný, spolehlivý a povinný postup pro tuto kritickou aktualizaci.

Základní problém, který řeší, je zajištění, že PGW udržuje přesné a včasné mapování mezi IP adresou UE (ukotvenou v PGW) a aktuálním koncovým bodem GTP-U tunelu (SGW) pro doručování downlink provozu. Bez explicitní notifikace, jako je UPN, by PGW mohlo i po předávání pokračovat v odesílání paketů na předchozí SGW, což by způsobilo ztrátu paketů. Protokol UPN zajišťuje plynulé předávání a kontinuitu služeb, což jsou základní požadavky pro mobilní širokopásmové služby. Jeho zavedení ve verzi 11 bylo součástí širšího úsilí o upevnění a optimalizaci signalizačních procedur EPC pro sítě LTE.

## Klíčové vlastnosti

- Definována jako typ zprávy GTPv2-C pro rozhraní S5/S8
- Používá se k notifikaci PGW o změnách stavu SGW (např. přemístění SGW, restart)
- Nese kritické informační prvky jako Cause a F-TEID SGW
- Spouští aktualizaci kontextu přenosových kanálů a směrovacích informací v PGW
- Vyžaduje potvrzení (UPA) od PGW
- Nezbytná pro udržení kontinuity relace během mobility UE

## Související pojmy

- [SGW – Signalling Gateway](/mobilnisite/slovnik/sgw/)
- [PGW – PDN Gateway](/mobilnisite/slovnik/pgw/)

## Definující specifikace

- **TS 29.275** (Rel-19) — PMIPv6 Mobility & Tunnelling Protocols Stage 3

---

📖 **Anglický originál a plná specifikace:** [UPN na 3GPP Explorer](https://3gpp-explorer.com/glossary/upn/)
