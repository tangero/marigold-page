---
slug: "lpi"
url: "/mobilnisite/slovnik/lpi/"
type: "slovnik"
title: "LPI – LCS Privacy Indicator"
date: 2025-01-01
abbr: "LPI"
fullName: "LCS Privacy Indicator"
category: "Security"
segment: "Services"
canonical: "https://3gpp-explorer.com/glossary/lpi/"
summary: "Mechanismus pro řízení ochrany soukromí v lokalizačních službách 3GPP (LCS), který udává, zda lze zveřejnit informace o poloze uživatele. Jedná se o parametr nastavený v UE nebo síti, který řídí autor"
---

LPI (indikátor ochrany soukromí LCS) je parametr pro řízení ochrany soukromí v lokalizačních službách 3GPP, který udává, zda lze zveřejnit polohu uživatele, a řídí autorizaci lokalizačních požadavků za účelem prevence neoprávněného sledování.

## Popis

[LCS](/mobilnisite/slovnik/lcs/) Privacy Indicator (LPI) je bezpečnostní a ochranný parametr v rámci architektury lokalizačních služeb 3GPP (LCS), zavedený ve verzi 16. Funguje jako příznak neboli indikátor, který specifikuje preference účastníka týkající se ochrany soukromí v souvislosti se zveřejňováním jeho lokalizačních informací žadatelům, jako jsou záchranné služby, poskytovatelé služeb s přidanou hodnotou nebo orgány pro zákonné odposlechy. Z architektonického hlediska je LPI uložen a spravován na dvou hlavních místech: v samotném uživatelském zařízení (UE) jako součást aplikace USIM nebo nastavení zařízení a v jádru sítě 5G, konkrétně ve funkci Unified Data Management ([UDM](/mobilnisite/slovnik/udm/)) nebo na serveru Home Subscriber Server ([HSS](/mobilnisite/slovnik/hss/)). Když je lokalizační požadavek iniciován prostřednictvím Gateway Mobile Location Centre ([GMLC](/mobilnisite/slovnik/gmlc/)) nebo Network Exposure Function ([NEF](/mobilnisite/slovnik/nef/)), síť konzultuje LPI jako součást procedury ověření a autorizace ochrany soukromí.

Fungování LPI zahrnuje vícekrokovou kontrolu autorizace. Po přijetí lokalizačního požadavku na cílové UE GMLC dotazuje UDM/HSS, aby získal LCS předplatitelská data účastníka, která zahrnují nastavení LPI. LPI může mít typicky hodnoty jako 'Žádné omezení', 'Omezeno na konkrétní služby' nebo 'Výjimka ochrany soukromí' (např. pro tísňová volání). Pokud LPI indikuje omezení, síť musí vyhodnotit, zda je žadající klient (identifikovaný svým typem klienta a typem služby) v rámci těchto omezení autorizován. Pro LPI založené na UE může UE přímo odpovídat na síťové dotazy na polohu svým nastavením ochrany soukromí, zejména ve scénářích zahrnujících lokalizační řešení na uživatelské rovině. Tyto pravidla může vynucovat také Privacy Profile Register (PPR) nebo vyhrazený LCS klient v síti, což zajišťuje, že informace o poloze jsou zveřejňovány pouze v souladu s preferencemi účastníka a regulačními požadavky.

Klíčové komponenty zahrnují UDM/HSS, které ukládají LPI jako součást profilu účastníka; GMLC, které funguje jako brána pro externí lokalizační požadavky a vynucuje kontroly ochrany soukromí; UE, které může uchovávat lokální kopii LPI; a [LMF](/mobilnisite/slovnik/lmf/), které může brát LPI v úvahu při navazování lokalizační relace. Role LPI je klíčová v širším bezpečnostním rámci LCS, neboť poskytuje standardizovaný mechanismus pro implementaci 'ochrany soukromí již při návrhu' v mobilních sítích. Pomáhá sítím dodržovat přísné předpisy na ochranu dat, jako je GDPR, tím, že zajišťuje, že zveřejnění polohy je vždy podmíněno výslovným nebo předpokládaným souhlasem uživatele, a tím předchází zneužití lokalizačních dat ke stalkingu, neoprávněné reklamě nebo jiným narušením soukromí.

## K čemu slouží

[LCS](/mobilnisite/slovnik/lcs/) Privacy Indicator byl zaveden, aby řešil rostoucí obavy o soukromí uživatelů a potenciál zneužití mobilních lokalizačních dat. Jak se služby založené na poloze ([LBS](/mobilnisite/slovnik/lbs/)) stávaly rozšířenějšími, sítě potřebovaly standardizovaný způsob správy a vynucování preferencí účastníků v oblasti ochrany soukromí nad rámec základních kontrol předplatného. Před LPI byly kontroly ochrany soukromí často specifické pro implementaci nebo omezené na jednoduché binární příznaky souhlasu, kterým chyběla podrobnost pro rozlišení mezi různými žadateli (např. záchranné služby vs. komerční aplikace). LPI poskytuje flexibilnější a standardizovaný indikátor, který je integrován do autorizačního rámce 3GPP LCS.

Problém, který řeší, je riziko neoprávněného sledování a zveřejňování polohy, což může vést k závažným narušením soukromí. Bez jasného, sítí vynucovaného indikátoru ochrany soukromí by mohli potenciálně získávaní lokalizaci účastníka bez patřičného souhlasu zlí aktéři nebo příliš vlezlé služby. LPI umožňuje účastníkům nastavit preference, které jsou přenášeny s jejich profilem, a zajišťuje tak konzistentní vynucování napříč různými přístupy do sítě (3G, 4G, 5G) a navštívenými sítěmi. Je obzvláště důležitý pro dodržování předpisů, protože mnoho jurisdikcí ukládá telekomunikačním operátorům povinnost získat výslovný souhlas uživatele se sdílením polohy, s výjimkou specifických případů, jako jsou tísňová volání nebo zákonný odposlech.

Motivace pro LPI také vychází z vývoje architektury LCS směrem k rozhraním založeným na službách v 5GC, což zvýšilo vystavení lokalizačních schopností aplikacím třetích stran prostřednictvím NEF. To zvýšilo potřebu robustních, standardizovaných kontrol ochrany soukromí. Definováním LPI ve verzi 16 poskytla 3GPP mechanismus připravený na budoucnost, který funguje s oběma metodami určování polohy na řídicí i uživatelské rovině a je v souladu s širšími vylepšeními ochrany soukromí, jako je ověřování ochrany soukromí založené na UE. Zajišťuje, že s tím, jak se zvyšuje přesnost lokalizace a objevují se nové případy užití, zůstává základní ochrana soukromí účastníka zachována v rámci síťové architektury.

## Klíčové vlastnosti

- Udává preference účastníka v oblasti ochrany soukromí pro zveřejnění polohy v rámci procedur 3GPP LCS.
- Uložen v síťových entitách (UDM/HSS) a volitelně v UE za účelem konzistentního vynucování pravidel.
- Integruje se do autorizačních toků LCS, aby povolil nebo zamítl lokalizační požadavky na základě typu klienta a služby.
- Podporuje podrobné nastavení, jako je neomezené, omezené na konkrétní služby nebo výjimky ochrany soukromí pro tísňové případy.
- Umožňuje dodržování předpisů na ochranu dat poskytováním standardizovaného mechanismu souhlasu.
- Funguje napříč lokalizačními řešeními na řídicí i uživatelské rovině v sítích 4G a 5G.

## Související pojmy

- [LCS – Location Services](/mobilnisite/slovnik/lcs/)
- [GMLC – Gateway Mobile Location Center](/mobilnisite/slovnik/gmlc/)
- [UDM – Unified Data Management](/mobilnisite/slovnik/udm/)
- [NEF – Network Exposure Function](/mobilnisite/slovnik/nef/)

## Definující specifikace

- **TS 23.273** (Rel-19) — 5G Location Services Stage 2 Architecture
- **TS 29.503** (Rel-19) — UDM Service Based Interface Stage 3
- **TS 37.890** (Rel-19) — Feasibility Study on 6 GHz for LTE/NR

---

📖 **Anglický originál a plná specifikace:** [LPI na 3GPP Explorer](https://3gpp-explorer.com/glossary/lpi/)
