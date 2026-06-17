---
slug: "crn"
url: "/mobilnisite/slovnik/crn/"
type: "slovnik"
title: "CRN – Call Request with Number"
date: 2025-01-01
abbr: "CRN"
fullName: "Call Request with Number"
category: "Services"
segment: "User Equipment"
canonical: "https://3gpp-explorer.com/glossary/crn/"
summary: "Doplňková služba umožňující uživateli vyžádat si volání na konkrétní číslo bez jeho přímého vytáčení. Umožňuje síťově iniciované zřízení hovoru na základě uložených nebo poskytnutých čísel a podporuje"
---

CRN je doplňková služba, která umožňuje uživateli vyžádat si síťově iniciované volání na konkrétní uložené číslo bez jeho přímého vytáčení.

## Popis

Call Request with Number (CRN) je doplňková služba definovaná v 3GPP TS 27.002, která umožňuje uživateli požádat síť o zřízení hovoru na konkrétní cílové číslo bez nutnosti ručního vytáčení kompletního čísla uživatelem. Služba funguje v rámci prostředí Mobile Station Application Execution Environment (MExE) a využívá mechanismus Unstructured Supplementary Service Data (USSD) pro komunikaci mezi mobilní stanicí a sítí. CRN funguje tak, že uživateli umožňuje uložit si často používaná čísla v síti nebo v mobilním zařízení a poté iniciovat hovory výběrem těchto uložených položek namísto zadávání plných telefonních čísel.

Technická implementace CRN zahrnuje několik klíčových komponent spolupracujících dohromady. Mobilní stanice obsahuje klientskou aplikaci CRN, která komunikuje s uživatelem, zatímco na straně sítě je funkce serveru CRN, typicky implementovaná v Home Location Register ([HLR](/mobilnisite/slovnik/hlr/)) nebo v dedikované služební uzlu. Když uživatel aktivuje CRN, mobilní stanice odešle USSD zprávu obsahující požadavek CRN do sítě. Tato zpráva obsahuje parametry jako kód služby, index uloženého čísla (při použití uložených čísel) nebo kompletní cílové číslo, pokud je poskytnuto přímo. Síť tento požadavek zpracuje, ověří uživatelovo předplatné služby CRN a poté zahájí proceduru zřizování hovoru na zadaný cíl.

CRN funguje prostřednictvím strukturované výměny protokolu definované ve specifikacích 3GPP. Služba podporuje více způsobů vyvolání: uživatelé si mohou vybrat ze seznamu předem uložených čísel ve svém profilu nebo zadat kompletní telefonní číslo během žádosti. Síť udržuje uložená čísla v uživatelském služebním profilu, kterým lze spravovat prostřednictvím samostatných provizních procedur. Při zpracování žádosti CRN síť provede autentizaci účastníka, autorizaci služby a validaci čísla před přistoupením k zřízení hovoru. Služba je integrována s existujícími procedurami řízení hovoru, což zajišťuje kompatibilitu se standardním zřizováním hovoru iniciovaného mobilní stanicí a zároveň přidává vrstvu abstrakce pro ukládání a načítání čísel.

Architektura služby podporuje scénáře iniciované mobilní stanicí i scénáře iniciované sítí. V případě iniciovaném mobilní stanicí uživatel explicitně žádá o hovor prostřednictvím rozhraní CRN. Síť také může využít schopnosti CRN k implementaci funkcí jako služby zpětného volání, kdy síť automaticky zřídí hovor na dříve pokusem nedosažený cíl. Integrace CRN s USSD zajišťuje spolehlivé doručování služebních požadavků i tehdy, když je uživatel zaměstnán jinou činností, jako je hovor, protože USSD funguje na signalizačním kanále namísto na kanálu pro přenos hovoru. To činí CRN zvláště užitečnou pro implementaci funkcí rychlého vytáčení a automatizovaných služeb volání v rámci ekosystému mobilní sítě.

## K čemu slouží

CRN byla vyvinuta k řešení potřeby zjednodušených procedur volání v mobilních sítích, zejména když se mobilní zařízení stávala složitějšími a uživatelé potřebovali spravovat rostoucí počet kontaktů. Před CRN museli uživatelé ručně vytáčet kompletní telefonní čísla pro každý hovor, což bylo zdlouhavé pro často kontaktovaná čísla nebo v situacích, kdy bylo nutné rychlé vytáčení. Služba si kladla za cíl snížit chyby při vytáčení, šetřit čas a zlepšit celkový uživatelský zážitek poskytnutím vrstvy abstrakce mezi uživatelem a složitými procedurami vytáčení.

Vytvoření CRN bylo motivováno rostoucím přijetím doplňkových služeb v sítích GSM a UMTS, kde operátoři usilovali o diferenciaci své nabídky prostřednictvím služeb s přidanou hodnotou. Tradiční řešení zkráceného vytáčení byla často implementována pouze v koncovém zařízení, což omezovalo jejich funkčnost, když uživatelé měnili zařízení nebo potřebovali síťové funkce. CRN poskytla standardizované síťové řešení, které fungovalo konzistentně napříč různými zařízeními a síťovými podmínkami. Tato standardizace byla zvláště důležitá s rostoucím rozšířením roamingu, protože zajišťovala, že uživatelé mohou přistupovat ke svým uloženým číslům a funkcím rychlého vytáčení bez ohledu na svou polohu nebo obsluhující síť.

CRN také řešila konkrétní případy užití, které bylo obtížné implementovat s existujícími mechanismy. Pro tísňové služby nebo často volaná čísla CRN umožňovala jednoúhozové vytáčení bez nutnosti, aby si uživatel musel pamatovat nebo vyhledat kompletní číslo. Služba podporovala obchodní aplikace, kde zaměstnanci potřebovali rychlý přístup k interním linkám nebo číslům zákaznické podpory. Díky integraci s infrastrukturou řízení služeb sítě mohlo být CRN kombinováno s dalšími doplňkovými službami, jako je přesměrování hovoru nebo čekání na hovor, čímž vznikaly sofistikovanější telefonní aplikace. Návrh služby zohledňoval omezení raných mobilních rozhraní a poskytoval řešení, které efektivně fungovalo i na zařízeních s omezenými možnostmi zobrazení nebo metodami vstupu.

## Klíčové vlastnosti

- Síťové ukládání a načítání čísel
- Vyvolání a řízení služby založené na USSD
- Podpora uložených čísel i přímého zadání čísla
- Integrace se standardními postupy zřizování hovoru
- Kompatibilita s roamingem napříč různými sítěmi
- Současný provoz s dalšími doplňkovými službami

## Související pojmy

- [HLR – Home Location Register](/mobilnisite/slovnik/hlr/)

## Definující specifikace

- **TS 27.002** (Rel-19) — Terminal Adaptation Functions for Asynchronous Services

---

📖 **Anglický originál a plná specifikace:** [CRN na 3GPP Explorer](https://3gpp-explorer.com/glossary/crn/)
