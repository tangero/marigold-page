---
slug: "nitz"
url: "/mobilnisite/slovnik/nitz/"
type: "slovnik"
title: "NITZ – Network Identity and Time Zone"
date: 2025-01-01
abbr: "NITZ"
fullName: "Network Identity and Time Zone"
category: "Services"
segment: "Core Network"
canonical: "https://3gpp-explorer.com/glossary/nitz/"
summary: "Služba umožňující mobilní síti poskytovat mobilním zařízením informace o místním čase, datu a časovém pásmu. Zajišťuje, že zařízení automaticky zobrazují správný místní čas bez manuální konfigurace už"
---

NITZ je služba, která umožňuje mobilní síti poskytovat místní čas, datum a informace o časovém pásmu mobilním zařízením pro automatické nastavení času.

## Popis

Network Identity and Time Zone (NITZ) je služba definovaná ve standardech 3GPP, která umožňuje mobilní síti doručovat přesné informace o místním čase, datu a časovém pásmu do uživatelského zařízení (UE). Funguje tak, že síť (konkrétně entity jádra sítě, jako je [MSC](/mobilnisite/slovnik/msc/) nebo [MME](/mobilnisite/slovnik/mme/)/[AMF](/mobilnisite/slovnik/amf/)) odešle tyto informace do UE pomocí signalizačních protokolů během procedur, jako je registrace polohy, sestavení hovoru, nebo prostřednictvím vyhrazených zpráv. UE tato data přijme a použije je k automatickému nastavení a aktualizaci svého vnitřního hodinového reálného času a kalendáře, čímž zajišťuje zobrazení správného místního času pro aktuální geografickou polohu uživatele.

Z architektonického hlediska je funkce NITZ součástí řídicí roviny jádra sítě. V obvodu spínaných ([CS](/mobilnisite/slovnik/cs/)) doménách ji typicky poskytuje Mobile Switching Center (MSC), zatímco v paketově spínaných ([PS](/mobilnisite/slovnik/ps/)) doménách ji může podporovat Mobility Management Entity (MME) v 4G nebo Access and Mobility Management Function (AMF) v 5G. Služba využívá existující [NAS](/mobilnisite/slovnik/nas/) (Non-Access Stratum) nebo jiné zprávy signalizace vrstvy 3 k přenosu informací NITZ. Přenášené informace zahrnují místní čas (často vztažený ke koordinovanému světovému času, [UTC](/mobilnisite/slovnik/utc/)), datum, posun pro letní čas ([DST](/mobilnisite/slovnik/dst/)), je-li aplikovatelný, a deskriptor časového pásma. Řídicí vrstva UE tyto informace zpracuje a podle toho upraví systémový čas zařízení.

Klíčovými komponentami jsou síťová entita, která generuje časová data (a která se může synchronizovat s přesným časovým zdrojem, jako je GNSS nebo NTP), signalizační protokol přenášející data NITZ (definovaný ve specifikacích jako TS 24.501 pro 5GS) a časový manažer klienta v UE. Zprávy NITZ mohou být odeslány sítí nevyžádaně nebo na žádost UE. Služba také podporuje doručování informací o identitě sítě, jako je název operátora, který může být zobrazen na UE. Tato dvojí funkce – poskytování času i identity sítě – se odráží v jejím názvu.

Úloha NITZ v síti spočívá v poskytování univerzální, sítí řízené služby synchronizace času pro mobilní zařízení. Je klíčová pro časové označování událostí, jako jsou záznamy hovorů pro účtování, umožnění časově závislých funkcí, jako jsou budíky, které přetrvají po restartu, a zajištění správného časového referenčního bodu pro aplikace. Odstraňuje závislost na uživateli, který by musel čas nastavovat manuálně, nebo na vnitřních hodinách zařízení, které mohou mít odchylku. Ve scénářích roamingu je NITZ obzvláště důležitá, protože umožňuje zařízení automaticky se přizpůsobit místnímu času navštívené sítě, čímž zvyšuje uživatelský komfort a přesnost služeb.

## K čemu slouží

NITZ byla vytvořena k řešení základního problému, kdy mobilní zařízení zobrazovala nesprávný místní čas, zejména po roamingu mezi časovými pásmy nebo po restartu. Před NITZ museli uživatelé ručně upravovat hodiny svých telefonů, což vedlo k chybám, zmeškaným schůzkám a komplikacím pro síťové operátory v účtování a poskytování časově vázaných služeb. Manuální přístup byl také nevhodný pro rostoucí složitost mobilních služeb a zvyšující se frekvenci mezinárodního cestování.

Služba řeší několik klíčových problémů: zajištění přesných záznamů pro účtování (záznamy podrobností hovoru s časovým razítkem správného místního síťového času), umožnění spolehlivých funkcí zařízení závislých na přesném čase (budíky, kalendáře) a poskytnutí lepší uživatelské zkušenosti automatizací správy času. Pro síťové operátory poskytuje mechanismus pro distribuci jediného, autoritativního časového referenčního bodu do všech zařízení v jejich síti, což je nezbytné pro provozní konzistenci a právní shodu v oblastech, jako je přesnost účtování.

Zavedená v 3GPP Release 4, NITZ navázala na dřívější, méně standardizované metody distribuce času. Její vývoj byl motivován globalizací mobilních sítí a potřebou bezproblémového roamingu. Standardizací informačních prvků a signalizačních procedur napříč různými generacemi sítí (od GSM/UMTS přes LTE až po 5G) zajistila NITZ zpětnou i dopřednou kompatibilitu. Vyřešila omezení spoléhání se na vnitřní hodiny reálného času UE (které mohou mít odchylku) nebo na externí necílové zdroje (které mohou být nedostupné nebo nezabezpečené), a poskytla tak spolehlivé, na síť zaměřené řešení integrované do základních procedur správy mobility.

## Klíčové vlastnosti

- Automaticky nastavuje místní čas, datum a časové pásmo na UE prostřednictvím síťové signalizace
- Podporuje doručování informací o identitě sítě (např. název operátora) pro zobrazení
- Funguje jak v obvodu spínaných, tak v paketově spínaných doménách jádra sítě
- Může být spuštěna registrací, aktualizací polohy nebo jinými událostmi mobility
- Zahrnuje informace o úpravě pro letní čas (DST)
- Poskytuje síťově autoritativní časový zdroj pro účtování a konzistenci služeb

## Související pojmy

- [NAS – Non-Access Stratum](/mobilnisite/slovnik/nas/)
- [MME – NPC MME Network Product Class](/mobilnisite/slovnik/mme/)
- [AMF – Access and Mobility Management Function](/mobilnisite/slovnik/amf/)
- [PLMN – Public Land Mobile Network](/mobilnisite/slovnik/plmn/)

## Definující specifikace

- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.251** (Rel-19) — Network Sharing Stage 2 Specification
- **TS 24.501** (Rel-19) — 5G NAS Protocols Specification
- **TS 33.303** (Rel-19) — ProSe Security Specification for EPS
- **TS 33.503** (Rel-19) — Security for Proximity Services (ProSe) in 5G

---

📖 **Anglický originál a plná specifikace:** [NITZ na 3GPP Explorer](https://3gpp-explorer.com/glossary/nitz/)
