---
slug: "bri"
url: "/mobilnisite/slovnik/bri/"
type: "slovnik"
title: "BRI – Binding Revocation Indication"
date: 2025-01-01
abbr: "BRI"
fullName: "Binding Revocation Indication"
category: "Protocol"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/bri/"
summary: "BRI je signalizační zpráva používaná v protokolu GPRS Tunneling Protocol (GTP) k explicitní žádosti o zrušení vazebních informací mezi síťovými uzly. Zajišťuje řádné vyčištění kontextů mobility a rela"
---

BRI je signalizační zpráva GTP, která explicitně žádá o zrušení vazebních informací mezi síťovými uzly, aby zajistila řádné vyčištění kontextů a zabránila zastaralým vazbám.

## Popis

Binding Revocation Indication (BRI, Indikace zrušení vazby) je kritická zpráva řídicí roviny v rámci protokolu [GPRS](/mobilnisite/slovnik/gprs/) Tunneling Protocol verze 2 (GTPv2), konkrétně definovaná pro rozhraní S5/S8 a S4 v architektuře Evolved Packet Core (EPC). Funguje jako mechanismus žádost-odpověď, kdy jeden síťový uzel (iniciátor) explicitně signalizuje druhému uzlu (příjemci), že konkrétní vazební informace musí být zneplatněny a přidružené zdroje uvolněny. Vazba (binding) v tomto kontextu označuje logické spojení udržované mezi síťovými entitami pro mobilní relaci konkrétního uživatelského zařízení (UE), které zahrnuje mapování mezi identitou UE, jeho aktuálním obslužným bránovým uzlem (SGW) a bránou paketové datové sítě (PGW).

Zpráva BRI obsahuje několik povinných a volitelných informačních prvků ([IE](/mobilnisite/slovnik/ie/)), které přesně identifikují, které vazby je třeba zrušit. Mezi nejkritičtější IE patří Cause, který udává důvod zrušení (např. odnětí předplatného, síťová porucha nebo zásah správce); plně kvalifikovaný identifikátor koncového bodu tunelu ([F-TEID](/mobilnisite/slovnik/f-teid/)) dotčeného přenosového kanálu; a případně identita mobilního zařízení ([MEI](/mobilnisite/slovnik/mei/)) nebo mezinárodní identifikace mobilního účastníka ([IMSI](/mobilnisite/slovnik/imsi/)) pro uživatelsky specifické vazby. Když uzel obdrží BRI, musí žádost zpracovat vyhledáním specifikovaného vazebního kontextu, ukončením jakéhokoli aktivního přenosu dat pro tento kontext, uvolněním přidružených zdrojů (jako je paměť a stavy časovačů) a odesláním zprávy Binding Revocation Acknowledgment ([BRA](/mobilnisite/slovnik/bra/)) jako potvrzení dokončení.

Z architektonického hlediska se BRI primárně vyměňuje mezi Serving Gateway (SGW) a Packet Data Network Gateway (PGW) na rozhraní S5/S8, ačkoli její použití se může rozšířit i na další rozhraní založená na [GTP](/mobilnisite/slovnik/gtp/), kde je vyžadována správa vazeb. Protokol zajišťuje spolehlivé doručení prostřednictvím standardních sekvenčních čísel GTP a mechanismů opakovaného přenosu. Z pohledu provozu sítě poskytuje BRI deterministický mechanismus čištění, který doplňuje implicitní čištění založené na vypršení časovače, což operátorům umožňuje aktivně spravovat stavy vazeb během údržby, při poruchových scénářích nebo v událostech životního cyklu účastníka bez nutnosti čekat na vypršení časovačů.

Zpracování BRI zahrnuje několik stavů protokolu: po přijetí platné BRI příjemce ověří žádost vůči své lokální databázi vazeb, zkontroluje autorizační politiky a provede proceduru zrušení, která zahrnuje upozornění všech závislých lokálních funkcí na odstranění vazby. Úspěšné zpracování vede k odeslání BRA s příčinou 'Request Accepted', zatímco při selhání (např. neexistující vazba nebo zamítnutí autorizace) se vrátí specifické chybové příčiny. Toto explicitní signalizace je obzvláště důležitá ve scénářích, kde více uzlů udržuje synchronizovaný stav o relaci UE, což zajišťuje, že všechny entity přejdou ke konzistentnímu pohledu při abnormálním ukončení relací.

## K čemu slouží

BRI byla zavedena, aby řešila problém zastaralých nebo osiřelých vazebních kontextů v mobilních sítích založených na [GTP](/mobilnisite/slovnik/gtp/), které mohly vést k vyčerpání zdrojů, nesprávnému směrování a degradaci služeb. Před jejím zavedením se čištění vazeb spoléhalo primárně na implicitní mechanismy, jako je vypršení časovačů nebo nepřímá signalizace prostřednictvím jiných procedur, které byly nedostatečné pro deterministickou správu zdrojů během síťových poruch nebo plánovaných operací. Absence explicitního protokolu pro zrušení znamenala, že sítě mohly během náhlých odpojení akumulovat neplatné vazby, což vytvářelo omezení škálovatelnosti a potenciální bezpečnostní zranitelnosti, kdy neoprávněné entity mohly zneužít přetrvávající kontexty.

Vytvoření BRI bylo motivováno evolucí směrem k architekturám čistě IP v 3GPP Release 8 (EPS), kde oddělení řídicí a uživatelské roviny a zavedení nových rozhraní jako S5/S8 vyžadovaly robustnější protokoly pro správu stavu. Jak se sítě stávaly dynamičtějšími s funkcemi jako mobilita mezi RAT, vícečetná připojení k PDN a později síťové segmenty, potřeba explicitní správy životního cyklu vazeb se stala klíčovou pro provozní spolehlivost. BRI poskytla operátorům nástroj pro aktivní správu síťových zdrojů, umožňující elegantní degradaci během údržby a rychlejší obnovu z poruchových scénářů ve srovnání s čekáním na dlouhé vypršení časovačů.

Z historické perspektivy BRI zaplnila mezeru v rodině protokolu GTP, která existovala od zavedení GPRS. Starší verze řešily čištění vazeb prostřednictvím kombinovaných procedur odstranění relace nebo spoléhaly na to, že mechanismy časovačů zdroje nakonec vyčistí. Tento přístup se ukázal jako nedostatečný pro sítě na úrovni operátora vyžadující dostupnost pěti devítek, kde by úniky zdrojů mohly časem narůstat a ovlivňovat stabilitu systému. Standardizovaný přístup BRI umožnil interoperabilní, na dodavateli nezávislou správu vazeb, která podporovala rostoucí komplexitu jader sítí 4G a 5G.

## Klíčové vlastnosti

- Explicitní signalizace pro zrušení vazby mezi uzly GTP
- Podpora více důvodů zrušení včetně správcovských, předplatitelských a poruchových scénářů
- Povinné zahrnutí F-TEID pro přesnou identifikaci přenosového kanálu
- Mechanismus spolehlivého doručení využívající sekvenční čísla GTP a potvrzení
- Integrace s bezpečnostními mechanismy GTPv2 pro autorizované zrušení
- Zpětně kompatibilní návrh, který nenarušuje stávající procedury GTP

## Související pojmy

- [GTP – GPRS Tunnelling Protocols](/mobilnisite/slovnik/gtp/)

## Definující specifikace

- **TS 29.275** (Rel-19) — PMIPv6 Mobility & Tunnelling Protocols Stage 3

---

📖 **Anglický originál a plná specifikace:** [BRI na 3GPP Explorer](https://3gpp-explorer.com/glossary/bri/)
