---
slug: "gca"
url: "/mobilnisite/slovnik/gca/"
type: "slovnik"
title: "GCA – Group Call Attributes"
date: 2025-01-01
abbr: "GCA"
fullName: "Group Call Attributes"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/gca/"
summary: "Atributy skupinového volání (GCA) jsou sada parametrů definovaných pro službu hlasového skupinového volání (VGCS) a službu hlasového vysílání (VBS) v GSM. Charakterizují skupinové volání včetně jeho i"
---

GCA je sada parametrů pro služby skupinového volání GSM (VGCS/VBS), která definuje identitu volání, prioritu, šifrovací režim a pravidla arbitráže mluvčího pro jeho zřízení a správu.

## Popis

Atributy skupinového volání (GCA) představují standardizovanou sadu parametrů v rámci specifikací GSM, která plně definuje konfiguraci a chování volání služby hlasového skupinového volání (VGCS) nebo služby hlasového vysílání (VBS). Definovány v dokumentu 3GPP TS 43.068 jsou tyto atributy uloženy v síti, typicky v registru skupinového volání ([GCR](/mobilnisite/slovnik/gcr/)) asociovaném s ústřednou mobilních služeb ([MSC](/mobilnisite/slovnik/msc/)), a používají je různé síťové elementy k zřizování a řízení relací skupinové komunikace. Skupinové volání je identifikováno referencí skupinového volání, která je spojena s jeho konkrétní sadou GCA.

Architektura zahrnuje MSC, základnový stanicový systém ([BSS](/mobilnisite/slovnik/bss/)) a mobilní stanice ([MS](/mobilnisite/slovnik/ms/)). Při zahájení skupinového volání vyzvedne původní MSC příslušné GCA pro specifikovanou skupinovou identitu z GCR. Tyto atributy jsou pak použity ke konfiguraci volání v celé síti. Mezi klíčové síťové elementy využívající GCA patří MSC pro směrování volání a servisní logiku, [BSC](/mobilnisite/slovnik/bsc/) pro správu rádiových zdrojů a řízení mluvčího a [BTS](/mobilnisite/slovnik/bts/) pro vlastní rádiový přenos na kanálu skupinového volání. Atributy jsou také zaslány zapojeným mobilním stanicím, aby rozuměly parametrům volání, jako je například režim pouze pro příjem (vysílání) nebo režim mluvení a příjmu (skupinové volání).

Jak to funguje: Parametry GCA jsou rozesílány během procedury zřizování skupinového volání. Například když uživatel zahájí skupinové volání vytočením skupinového ID, MSC načte odpovídající GCA. Poté použije tyto atributy k tomu, aby nařídila BSC přidělit pro volání komunikační kanál (TCH), určila seznam buněk, kde má být volání aktivní, a aplikovala správný šifrovací algoritmus. BSC využívá atributy 'Priorita mluvčího' a 'Arbitráž mluvčího' ke správě žádostí od více uživatelů, kteří chtějí hovořit (přístup na uplink). Mobilní stanice přijímají relevantní informace GCA v zřizovací zprávě, což jim umožňuje připojit se na správný kanál, aplikovat správný šifrovací klíč a pochopit pravidla pro žádost o uplink.

Jeho role je klíčová pro sadu funkcí VGCS/VBS, neboť poskytuje flexibilní a parametrizovaný způsob podpory různých potřeb skupinové komunikace. Oddělením skupinové identity od pevné sady chování umožňuje GCA jedné síťové infrastruktuře podporovat nespočet skupin – z nichž každá může mít potenciálně odlišné úrovně zabezpečení, geografický rozsah a uživatelská oprávnění. Díky tomu je GSM životaschopnou platformou pro hlasové služby kritické pro činnost, používané složkami integrovaného záchranného systému, dopravními společnostmi a podniky technické infrastruktury.

## K čemu slouží

GCA bylo vytvořeno za účelem umožnění efektivních a funkčně bohatých služeb skupinové komunikace v rámci standardu GSM, konkrétně pro službu hlasového skupinového volání (VGCS) a službu hlasového vysílání (VBS). Před formalizací těchto atributů vyžadovalo poskytování konfigurovatelných skupinových volání proprietární implementace, což bránilo interoperabilitě mezi síťovými zařízeními od různých dodavatelů a mezi skupinami uživatelů přicházejících do jiných sítí (roaming). Rámec GCA tento problém vyřešil standardizací základních charakteristik skupinového volání.

Primární problém, který řeší, je potřeba škálovatelného a spravovatelného systému pro podporu funkcí podobných profesionální mobilní radiokomunikaci (PMR) na veřejné celulární síti. Organizace, jako jsou policie, hasičské záchranné sbory nebo železniční dopravci, vyžadují okamžitou skupinovou komunikaci, kdy jedna osoba mluví a mnoho naslouchá, často se specifickými požadavky na oblast volání, prioritu nad běžným provozem a zabezpečení. GCA poskytuje technický plán pro splnění těchto požadavků v rámci architektury GSM, což operátorům sítí umožňuje nabízet konkurenceschopnou alternativu k tradičním systémům PMR, jako je TETRA.

Historicky byl vývoj VGCS/VBS a GCA v Release 8 (i když navazoval na dřívější práci) motivován rostoucí poptávkou trhu po skupinové komunikaci a snahou využít rozsáhlé pokrytí sítí GSM. Řešil omezení základního konferenčního hovoru, který je náročný na zdroje a postrádá rychlé zřízení a geografické cílení potřebné pro operační komunikaci. Definováním atributů jako 'Oblast skupinového volání', 'Šifrovací algoritmus' a 'Identifikace mluvčího' zajistilo GCA, že skupinová volání mohou být zabezpečená, efektivně spravovaná z hlediska rádiových zdrojů a přizpůsobená specifickým operačním pravidlům předplatitelské organizace.

## Klíčové vlastnosti

- Definuje kompletní sadu parametrů pro konfiguraci volání VGCS a VBS
- Zahrnuje referenci skupinového volání, šifrovací algoritmus a skupinový klíč pro zabezpečení
- Specifikuje pravidla priority mluvčího a arbitráže pro správu uplinku
- Určuje oblast skupinového volání (seznam buněk) pro geografické cílení
- Podporuje jak režim vysílání (pouze příjem), tak režim skupinového volání (mluvení a příjem)
- Parametry jsou uloženy v registru skupinového volání (GCR) pro konzistenci v celé síti

## Související pojmy

- [GSM – Global System for Mobile Communications](/mobilnisite/slovnik/gsm/)

## Definující specifikace

- **TS 43.068** (Rel-19) — Voice Group Call Service (VGCS) Stage 2

---

📖 **Anglický originál a plná specifikace:** [GCA na 3GPP Explorer](https://3gpp-explorer.com/glossary/gca/)
