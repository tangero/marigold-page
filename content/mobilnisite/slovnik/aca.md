---
slug: "aca"
url: "/mobilnisite/slovnik/aca/"
type: "slovnik"
title: "ACA – Accounting Answer"
date: 2025-01-01
abbr: "ACA"
fullName: "Accounting Answer"
category: "Management"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/aca/"
summary: "ACA je zpráva protokolu založeného na Diameteru používaná v systému Online Charging System (OCS) podle 3GPP. Je to odpověď od OCS na síťový prvek (např. P-GW, S-CSCF) na přidělení nebo zamítnutí kredi"
---

ACA je zpráva protokolu Diameter, která představuje odpověď Online Charging Systemu na síťový prvek, přidělující nebo zamítající kredit pro uživatelskou služební relaci za účelem umožnění fakturace v reálném čase.

## Popis

Accounting Answer (ACA) je klíčový aplikační příkaz Diameter v referenčních bodech Ro a Gy podle 3GPP, definovaný v rámci Diameter Credit-Control Application ([DCCA](/mobilnisite/slovnik/dcca/)) (RFC 4006). Funguje jako konečná odpověď od Online Charging Systemu ([OCS](/mobilnisite/slovnik/ocs/)) na předchozí Accounting Request ([ACR](/mobilnisite/slovnik/acr/)) odeslaný síťovou funkcí fungující jako Diameter klient, například Policy and Charging Enforcement Function (PCEF) v [P-GW](/mobilnisite/slovnik/p-gw/) nebo Application Function ([AF](/mobilnisite/slovnik/af/)). Zpráva ACA nese rozhodnutí OCS ohledně požadované kvóty služebních jednotek (např. objemu dat, časového trvání nebo peněžního kreditu) pro konkrétní uživatelskou služební relaci.

Z architektonického hlediska je ACA součástí řídicího dialogu kreditní kontroly v reálném čase na bázi relací. Když uživatel zahájí datovou relaci nebo službu s přidanou hodnotou, síťový prvek (Diameter klient) odešle ACR (Initial, Intermediate, Update nebo Final) do OCS. OCS tento požadavek zpracuje vůči uživatelskému zůstatku na účtu a pravidlům politiky. Výsledná zpráva ACA obsahuje přidělenou kvótu, dobu její platnosti a konkrétní instrukce pro klienta. Mezi klíčové atributy ([AVP](/mobilnisite/slovnik/avp/)) uvnitř ACA patří Granted-Service-Unit AVP (určující přidělené množství dat, času nebo peněz), Validity-Time AVP, Result-Code AVP (udávající úspěch nebo konkrétní chybu) a Final-Unit-Indication AVP (která instruuje klienta o akcích, které má provést při vyčerpání přidělené kvóty, jako je ukončení přístupu nebo přesměrování na portál pro dobití).

Úlohou ACA je vynucovat fakturační politiku OCS v reálném čase. Po přijetí ACA síťový prvek aplikuje přidělenou kvótu na uživatelskou relaci a sleduje její spotřebu. Když se kvóta blíží vyčerpání, klient odešle nový ACR (Update), aby požádal o další kredit, což spustí další ACA odpověď. Tento nepřetržitý cyklus požadavek-odpověď umožňuje přesnou a okamžitou kontrolu využití zdrojů a výdajových limitů. Pro konečný ACR signalizující ukončení relace odpovídající ACA potvrzuje uzavření a může obsahovat konečná účtovací data pro vyúčtování. ACA je tedy mechanismus, který překládá fakturační politiky vysoké úrovně na proveditelná přidělení zdrojů pro každou relaci, což umožňuje předplacené, na požádání a konvergentní fakturační modely.

## K čemu slouží

ACA existuje za účelem umožnění fakturace v reálném čase (online charging) v sítích 3GPP, což je základní požadavek pro moderní telekomunikační služby, zejména předplacené nabídky. Před standardizovanou online fakturaci bylo účtování často dávkově zpracovávanou offline záležitostí, kde se záznamy o využití ([CDR](/mobilnisite/slovnik/cdr/)) shromažďovaly a zpracovávaly po skončení relace. To vytvářelo pro operátory významné úvěrové riziko, protože uživatelé mohli nashromáždit poplatky přesahující zůstatek na účtu, a bránilo to reálné kontrole služeb, jako jsou výdajové limity nebo okamžité dobití kvót. Zavedení [OCS](/mobilnisite/slovnik/ocs/) založeného na Diameteru s dialogem ACA/ACR tyto problémy vyřešilo vytvořením přímého protokolu pro autorizaci kreditu během relace.

Vytvoření ACA bylo motivováno potřebou bezpečného, spolehlivého a standardizovaného signalizačního mechanismu mezi síťovými prvky a fakturačním systémem. Řeší omezení 'slepého' poskytování služeb vložením bodu rozhodování o politice (OCS) přímo do cesty řízení služby. ACA poskytuje autoritativní odpověď 'ano/ne' a 'kolik', která řídí, zda může uživatel nadále používat službu. To umožňuje nejen předplacené účtování, ale také sofistikované postpaidové kontroly, jako jsou výdajové stropy, oznámení v reálném čase a bezproblémová integrace služeb pro hlas, video a zasílání zpráv založené na IMS. Její standardizace napříč vydáními 3GPP zajistila interoperabilitu mezi zařízeními od různých výrobců, což bylo klíčové pro nasazení složitých vícevýrobkových sítí LTE a 5G.

## Klíčové vlastnosti

- Přenáší přidělenou kvótu (data, čas, peníze) z OCS na síťový prvek
- Používá standardizovaný protokol Diameter s konkrétními AVP definovanými v 3GPP TS 32.299
- Podporuje více typů služebních jednotek (CC-Total-Octets, CC-Time, CC-Money) v rámci AVP Granted-Service-Unit
- Obsahuje Validity-Time AVP pro vynucení časového vypršení platnosti kvóty
- Přenáší Final-Unit-Indication, aby instruovala klienta o akcích při vyčerpání kvóty
- Přenáší Result-Code AVP udávající úspěch (DIAMETER_SUCCESS) nebo konkrétní chyby Diameteru

## Definující specifikace

- **TS 32.260** (Rel-19) — IMS Charging Management
- **TS 32.272** (Rel-19) — Charging for Push-to-Talk over Cellular (PoC)
- **TS 32.273** (Rel-19) — MBMS Charging Management
- **TS 32.278** (Rel-19) — Monitoring Events Offline Charging Specification
- **TS 32.299** (Rel-19) — Diameter Charging Applications for 3GPP

---

📖 **Anglický originál a plná specifikace:** [ACA na 3GPP Explorer](https://3gpp-explorer.com/glossary/aca/)
