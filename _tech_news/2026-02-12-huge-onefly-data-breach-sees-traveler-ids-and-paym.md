---
author: Marisa Aigen
category: únik dat
companies:
- OneFly
date: '2026-02-12 15:42:16'
description: Plné platební údaje v čistém textu unikly z nechráněné instance Elasticsearch,
  postihuje nejméně 6000 zákazníků OneFly. Mezi uniklými daty jsou jména, data narození,
  detaily identifikačních dokladů, údaje o letech a JWT tokeny.
importance: 5
layout: tech_news_article
original_title: Huge OneFly data breach sees traveler IDs and payment details leaked
publishedAt: '2026-02-12T15:42:16+00:00'
slug: huge-onefly-data-breach-sees-traveler-ids-and-paym
source:
  emoji: 📰
  id: techradar
  name: TechRadar
title: 'Obrovský únik dat OneFly: Unikly identifikační údaje cestujících a platební
  detaily'
url: https://www.techradar.com/pro/security/huge-onefly-data-breach-sees-traveler-ids-and-payment-details-leaked
urlToImage: https://cdn.mos.cms.futurecdn.net/jt92kXfBXVXUWwnKBmDJLn-2560-80.jpg
urlToImageBackup: https://cdn.mos.cms.futurecdn.net/jt92kXfBXVXUWwnKBmDJLn-2560-80.jpg
---

## Souhrn
Společnost OneFly, poskytovatel technologických řešení pro cestovní ruch a agregátor leteckých jízdenek, unikla tisíce citlivých záznamů zákazníků prostřednictvím nechráněné instance Elasticsearch. Bezpečnostní výzkumníci z Cybernews objevili v reálném čase data z devíti interních Java Spring aplikací, včetně plných detailů platebních karet v čistém textu. Postižení jsou nejméně 6000 zákazníků s platidly a kolem 10 000 identifikačních záznamů.

## Klíčové body
- Unikla data z nechráněné Elasticsearch instance: jména, data narození, detaily ID dokladů, čísla letů, ceny jízdenek, destinace, plné údaje kreditních karet a JWT tokeny.
- Zdroj: Devět interních Java Spring aplikací, které vygenerovala data v reálném čase.
- Čas úniku: Důkazy ukazují na začátek října 2025, přesný rozsah a počet postižených není znám.
- Doporučení Cybernews: Zavést ovládání přístupu, vylepšené logování a bílou listu IP adres.
- OneFly: Globální agregátor cestovního obsahu a dodavatel leteckých jízdenek.

## Podrobnosti
Bezpečnostní tým Cybernews nedávno narazil na otevřenou Elasticsearch instanci, která v reálném čase odhalovala tisíce záznamů z interního systému OneFly. Elasticsearch je databázový systém navržený pro rychlé vyhledávání a analýzu velkých objemů dat, často používaný v backendu webových aplikací pro indexování a ukládání strukturovaných informací. V tomto případě nebyla instance zabezpečená autentizací, což umožnilo volný přístup z internetu.

Data pocházela z devíti Java Spring aplikací – Spring je framework pro vývoj robustních Java aplikací, běžně používaný pro webové služby, mikroslužby a enterprise systémy, kde zpracovává transakce jako rezervace letů. Mezi uniklými informacemi byly osobní údaje jako jména a data narození, detaily pasů nebo občanských průkazů (typ, číslo, platnost), údaje o letech (číslo, datum, odletové a příletové letiště, cena jízdenky) a zejména plné platební údaje včetně čísla karty, platnosti a pravděpodobně CVV kódu v čistém textu. JWT tokeny (JSON Web Tokens) slouží k autentizaci a autorizaci uživatelů v API, obsahují zakódované informace o session a mohou být zneužity k přihlášení do systémů.

OneFly se specializuje na agregaci cestovního obsahu z celého světa a dodávky leteckých jízdenek pro cestovní agentury a platformy. Není to přímý prodejce letenek koncovým zákazníkům, ale B2B dodavatel dat a služeb. Výzkumníci odhadují počet postižených na 10 000 identifikačních záznamů a 6000 platebních karet, což označili za "spíše minimální", ale riziko je vysoké – útočníci mohou tyto údaje použít k krádežím identity, podvodným transakcím nebo prodeji na dark webu. Přesný čas vzniku dat nelze určit, ale metadata naznačují říjen 2025. Cybernews společnost OneFly informoval, ale článek neuvádí reakci.

Takové úniky nechráněných databází jsou běžné kvůli chybám v konfiguraci cloudových služeb, kde vývojáři zapomenou nastavit firewall nebo autentizaci. Elasticsearch instances často běží na AWS nebo Azure bez defaultních bezpečnostních opatření, což vede k incidentům jako tento.

## Proč je to důležité
Tento incident podtrhuje systémové selhání v bezpečnosti cloudových databází, kde nechráněné instance Elasticsearch způsobily už stovky úniků milionů záznamů globálně. Pro cestovní průmysl to znamená okamžité riziko pro zákazníky – ukradené platební údaje umožňují neoprávněné nákupy, zatímco ID doklady usnadňují krádeže identity. V širším IT ekosystému zdůrazňuje nutnost zero-trust architektury: vždy ověřovat přístup, šifrovat data v klidu i v přenosu a monitorovat logy. Doporučení jako IP whitelisting (omezení přístupu jen na důvěryhodné IP) a role-based access control (RBAC) jsou standardy, které firmy ignorují na vlastní nebezpečí. Pro OneFly to může vést k regulátním pokutám pod GDPR (až 4 % globálního obratu) a ztrátě důvěry partnerů. V době rostoucích kybernetických hrozeb je takový únik signálem pro celý sektor, aby přehodnotil konfigurace databází a přijal automatizované nástroje pro detekci expozic, jako Shodan nebo cloud nativní skenery.

---

[Číst původní článek](https://www.techradar.com/pro/security/huge-onefly-data-breach-sees-traveler-ids-and-payment-details-leaked)

**Zdroj:** 📰 TechRadar
