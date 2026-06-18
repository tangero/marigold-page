---
slug: "slpp"
url: "/mobilnisite/slovnik/slpp/"
type: "slovnik"
title: "SLPP – Subscriber LCS Privacy Profile"
date: 2025-01-01
abbr: "SLPP"
fullName: "Subscriber LCS Privacy Profile"
category: "Services"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/slpp/"
summary: "Profil ochrany soukromí pro služby lokalizace (LCS), který definuje preference účastníka pro reportování polohy a ochranu soukromí. Umožňuje uživatelům řídit, kdo je může lokalizovat a za jakých podmí"
---

SLPP je profil ochrany soukromí služeb lokalizace (LCS) účastníka, který definuje jeho preference pro reportování polohy, řídí, kdo jej může lokalizovat a za jakých podmínek, aby byla zajištěna ochrana soukromí a souhlas.

## Popis

Subscriber [LCS](/mobilnisite/slovnik/lcs/) Privacy Profile (SLPP) je základní součást architektury služeb lokalizace (LCS) podle 3GPP, navržená k vynucování uživatelských preferencí ochrany soukromí pro lokalizační operace. Je uložen v síti, typicky v Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)) nebo v samostatném registru profilů ochrany soukromí, a přistupují k němu Gateway Mobile Location Centre ([GMLC](/mobilnisite/slovnik/gmlc/)) a další entity LCS. Profil obsahuje pravidla, která určují, zda má být žádost o polohu od konkrétního klienta (např. od služby s přidanou hodnotou, tísňové služby nebo orgánů činných v trestním řízení) povolena, zamítnuta, nebo zda vyžaduje výslovné upozornění a souhlas účastníka. Tato pravidla jsou vyhodnocována na základě parametrů, jako je identita a typ žadatele, typ lokalizační žádosti (např. okamžitá, odložená, periodická) a aktuální geografická oblast účastníka.

Operačně, když Location Service Client (LCS klient) zahájí žádost o polohu cílové mobilní stanice ([MS](/mobilnisite/slovnik/ms/)), je žádost směrována do GMLC. GMLC načte SLPP účastníka z HSS. Profil je následně zpracován, aby se určila příslušná kontrola ochrany soukromí. Výsledkem této kontroly může být schválení žádosti bez upozornění uživatele, schválení až po upozornění uživatele a získání souhlasu (např. přes [SMS](/mobilnisite/slovnik/sms/), [USSD](/mobilnisite/slovnik/ussd/) nebo datovou relaci), nebo přímé zamítnutí. SLPP podporuje různé třídy klientů, jako jsou tísňové služby, služby s přidanou hodnotou, orgány činné v trestním řízení a samotný účastník, přičemž každý může mít různou úroveň autorizace. Tato detailní kontrola je klíčová pro soulad s předpisy na ochranu soukromí, jako je GDPR, a pro budování důvěry uživatelů v lokalizační aplikace.

Architektura SLPP je integrována do signalizace jádra sítě, primárně využívá rozhraní založená na protokolu Diameter (např. mezi GMLC a HSS) nebo [MAP](/mobilnisite/slovnik/map/) (Mobile Application Part) ve starších vydáních. Je klíčovým prvkem pro komerční LCS služby, jako je vyhledávání přátel, správa vozového parku nebo lokalizační reklama, protože poskytuje právní a technický rámec pro uživatelský souhlas. Bez SLPP by sítě nemohly nabízet diferencované zacházení z hlediska ochrany soukromí, což by mohlo vést k neoprávněnému sledování a významným právním rizikům. Správa SLPP může být částečně zpřístupněna účastníkům prostřednictvím samoobslužných portálů, což uživatelům umožňuje dynamicky aktualizovat své preference ochrany soukromí.

## K čemu slouží

SLPP byl vytvořen, aby řešil kritické obavy o ochranu soukromí, které jsou vlastní lokalizačnímu sledování v celulárních sítích. Jak se mobilní sítě vyvíjely a poskytovaly přesnou polohu uživatele (zpočátku pro tísňové služby jako E911 v USA), bylo zřejmé, že by tato schopnost mohla být zneužita bez odpovídajících ochranných opatření. Před standardizovanými profily ochrany soukromí neexistoval jednotný mechanismus, který by účastníkům umožňoval řídit, kdo je může lokalizovat, což vytvářelo rizika neoprávněného sledování a porušování základních práv na soukromí. SLPP poskytuje standardizovanou, síťově vynucovanou metodu pro získání a respektování souhlasu uživatele.

K jeho vývoji vedly jak regulatorní tlaky, tak komerční potřeby. Regulátoři požadovali, aby telekomunikační operátoři chránili lokalizační data účastníků. Z komerčního hlediska potřebovali uživatelé pro rozvoj lokalizačních služeb ([LBS](/mobilnisite/slovnik/lbs/)) záruku, že jejich soukromí bude respektováno. SLPP to řeší tím, že dává kontrolu do rukou uživatele prostřednictvím konfigurovatelných profilů, což umožňuje důvěryhodný ekosystém pro LBS. Rozlišuje mezi různými žadateli a zajišťuje, že tísňová volání mohou být vždy lokalizována, zatímco komerční služby vyžadují výslovné povolení, čímž vyvažuje bezpečnost, zákonnost a inovace služeb.

## Klíčové vlastnosti

- Definuje autorizační pravidla pro lokalizační žádosti podle typu klienta (např. tísňové služby, služby s přidanou hodnotou, orgány činné v trestním řízení)
- Podporuje více metod upozornění a ověření (např. SMS, USSD, datová relace) pro získání souhlasu uživatele
- Umožňuje konfiguraci nastavení ochrany soukromí podle geografické oblasti nebo denní doby
- Uložen v HSS pro centralizovaný přístup a konzistenci v celé síti
- Integruje se s GMLC pro vynucování pravidel ochrany soukromí v reálném čase během lokalizačních procedur
- Umožňuje účastníkům spravovat preference ochrany soukromí prostřednictvím samoobslužných rozhraní

## Související pojmy

- [LCS – Location Services](/mobilnisite/slovnik/lcs/)
- [GMLC – Gateway Mobile Location Center](/mobilnisite/slovnik/gmlc/)
- [HSS – Home Subscriber Server](/mobilnisite/slovnik/hss/)

## Definující specifikace

- **TS 03.071** (Rel-7) — Location Services (LCS) Stage 2 Description
- **TR 21.905** (Rel-19) — 3GPP Technical Terms and Definitions
- **TS 23.271** (Rel-19) — LCS Stage 2 Specification
- **TS 23.586** (Rel-19) — Ranging & Sidelink Positioning in 5GS
- **TS 24.501** (Rel-19) — 5G NAS Protocols Specification
- **TS 24.514** (Rel-19) — Ranging & Sidelink Positioning in 5GS
- **TS 24.571** (Rel-19) — Control Plane LCS Procedures
- **TS 29.586** (Rel-19) — SLPKMF Service Based Interface Protocol
- **TS 33.533** (Rel-19) — Security for 5G Ranging & Sidelink Positioning
- **TS 37.571** (Rel-19) — UE Conformance for Positioning
- **TS 38.305** (Rel-19) — NG-RAN UE Positioning Stage 2
- **TS 38.355** (Rel-19) — Sidelink Positioning Protocol (SLPP)

---

📖 **Anglický originál a plná specifikace:** [SLPP na 3GPP Explorer](https://3gpp-explorer.com/glossary/slpp/)
