---
slug: "ppr"
url: "/mobilnisite/slovnik/ppr/"
type: "slovnik"
title: "PPR – Privacy Profile Register"
date: 2025-01-01
abbr: "PPR"
fullName: "Privacy Profile Register"
category: "Security"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/ppr/"
summary: "Privacy Profile Register (Registr profilů soukromí) je síťová funkce, která ukládá a spravuje nastavení a preference soukromí uživatele týkající se služeb určení polohy a zpřístupnění osobních údajů."
---

PPR je síťová funkce, která ukládá a spravuje nastavení soukromí uživatele za účelem řízení sdílení jeho polohy a osobních údajů a vynucuje politiky o tom, jaké informace jsou komu zveřejňovány.

## Popis

Privacy Profile Register (PPR, Registr profilů soukromí) je logická síťová entita definovaná v architektuře 3GPP pro správu soukromí uživatele, primárně v kontextu služeb určení polohy ([LCS](/mobilnisite/slovnik/lcs/)). Funguje jako databáze a bod vynucování politik, který uchovává preference soukromí účastníka, často označované jako 'profil soukromí'. Tento profil obsahuje pravidla, která určují podmínky, za kterých mohou být informace o poloze účastníka vyžádány, vypočteny a zveřejněny různým subjektům, známým jako LCS klienti.

PPR interaguje s několika prvky jádra sítě, aby tato pravidla vynutil. Když je služba určení polohy vyvolána LCS klientem (např. navigační aplikací, záchrannou službou nebo službou s přidanou hodnotou), je požadavek směrován přes Gateway Mobile Location Centre ([GMLC](/mobilnisite/slovnik/gmlc/)). GMLC dotazuje Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)), aby určil obsluhující uzel a získal LCS předplatitelská data účastníka. Klíčové je, že HSS může také uvést adresu PPR asociovanou s uživatelem. GMLC následně kontaktuje PPR, aby ověřil požadavek vůči uloženému profilu soukromí. Profil obsahuje pravidla založená na faktorech, jako je identita žádajícího klienta (typ klienta, identita), typ požadavku na polohu (např. okamžitý, odložený, periodický), požadovaná přesnost a denní doba.

Na základě vyhodnocení vrátí PPR GMLC verdikt: povoleno, zamítnuto nebo povoleno s notifikací. Pokud je povoleno, postup určení polohy pokračuje přes Mobile Switching Centre ([MSC](/mobilnisite/slovnik/msc/)) nebo Mobility Management Entity ([MME](/mobilnisite/slovnik/mme/))/Access and Mobility Management Function ([AMF](/mobilnisite/slovnik/amf/)) k UE. Pokud profil vyžaduje notifikaci, síť může před zveřejněním polohy odeslat upozornění na zařízení uživatele a vyžádat si souhlas. Pokud je zamítnuto, je požadavek odmítnut. PPR může být samostatný uzel, nebo může být jeho funkčnost integrována do HSS nebo jiného síťového úložiště. Jeho architektura centralizuje kontrolu soukromí a poskytuje konzistentní bod pro politiku bez ohledu na polohu uživatele nebo typ přístupové sítě (2G, 3G, 4G, 5G), kterou používá.

## K čemu slouží

PPR byl vytvořen, aby řešil rostoucí obavy o soukromí a regulatorní požadavky (např. GDPR v Evropě, různé národní zákony) týkající se sledování a zveřejňování zeměpisné polohy mobilního účastníka. Rané služby určení polohy postrádaly detailní uživatelskou kontrolu; jakmile se uživatel přihlásil k [LCS](/mobilnisite/slovnik/lcs/), mohla být jeho poloha potenciálně poskytnuta jakékoli autorizované službě bez dalšího souhlasu. To vyvolalo významné problémy se soukromím, protože uživatelé požadovali schopnost kontrolovat, kdo je může lokalizovat a kdy.

Jeho vývoj byl motivován potřebou standardizovat flexibilní, na uživatele zaměřený rámec pro správu soukromí v rámci telekomunikační sítě. Před konceptem PPR bylo soukromí často řešeno ad-hoc aplikacemi nebo bylo jednoduchým binárním příznakem předplatného v [HLR](/mobilnisite/slovnik/hlr/)/HSS. PPR zavádí sofistikovaný systém založený na pravidlech, který posiluje postavení účastníka. Řeší problém dynamické správy soukromí, umožňuje uživatelům nastavit různá pravidla pro různé žadatele (např. vždy povolit záchranné služby, povolit rodině pouze ve večerních hodinách, zakázat všechny komerční požadavky). To uživatelům poskytuje transparentnost a kontrolu, což je nezbytné pro etické a legální nasazení služeb založených na poloze, podporuje důvěru uživatelů a umožňuje růst ekosystému LCS.

## Klíčové vlastnosti

- Ukládá uživatelem definovaná pravidla soukromí (profily) pro zveřejňování informací o poloze
- Zachycuje a vyhodnocuje požadavky služby určení polohy od LCS klientů přes GMLC
- Podporuje vyhodnocování pravidel na základě identity klienta, typu požadavku, času a přesnosti
- Poskytuje verdikty: Povolit, Zakázat nebo Povolit s Notifikací/Ověřením
- Může být integrován s HSS nebo implementován jako samostatná síťová funkce
- Centralizuje vynucování politiky soukromí pro konzistentní uživatelský zážitek napříč síťovými doménami

## Související pojmy

- [LCS – Location Services](/mobilnisite/slovnik/lcs/)
- [GMLC – Gateway Mobile Location Center](/mobilnisite/slovnik/gmlc/)
- [HSS – Home Subscriber Server](/mobilnisite/slovnik/hss/)

## Definující specifikace

- **TS 23.271** (Rel-19) — LCS Stage 2 Specification
- **TS 23.871** (Rel-5) — Enhanced User Privacy for Location Services
- **TS 29.173** (Rel-19) — Diameter-based SLh Interface for LCS
- **TS 32.271** (Rel-19) — 3GPP LCS Charging Management Spec
- **TS 32.272** (Rel-19) — Charging for Push-to-Talk over Cellular (PoC)

---

📖 **Anglický originál a plná specifikace:** [PPR na 3GPP Explorer](https://3gpp-explorer.com/glossary/ppr/)
