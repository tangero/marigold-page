---
category: kybernetická bezpečn
companies:
- OpenAI
date: '2025-10-28 17:33:45'
description: Bezpečnostní výzkumníci zjistili, že prohlížeč Atlas od OpenAI je extrémně
  zranitelný vůči útokům typu prompt injection, a to i přes adresní řádek.
importance: 4
layout: tech_news_article
original_title: Serious New Hack Discovered Against OpenAI’s New AI Browser - Futurism
publishedAt: '2025-10-28T17:33:45+00:00'
slug: serious-new-hack-discovered-against-openais-new-ai
source:
  emoji: 📰
  id: null
  name: Futurism
title: Vážná bezpečnostní chyba objevena v novém AI prohlížeči od OpenAI
url: http://futurism.com/artificial-intelligence/serious-new-hack-openai-ai-browser
urlToImage: https://futurism.com/wp-content/uploads/2025/10/serious-new-hack-openai-ai-browser_236135.jpg?w=1200
urlToImageBackup: https://futurism.com/wp-content/uploads/2025/10/serious-new-hack-openai-ai-browser_236135.jpg?w=1200
---

## Souhrn

Bezpečnostní výzkumníci z firmy NeuralTrust odhalili kritickou zranitelnost v novém AI prohlížeči Atlas od OpenAI. Útočníci mohou prostřednictvím speciálně upravených URL adres vložených do adresního řádku (omnibox) prohlížeče provádět škodlivé příkazy, které prohlížeč vykoná s vysokou úrovní důvěry. Jde o nový typ útoku prompt injection, který nevyžaduje úpravu webových stránek, ale pouze zkopírování podvržené URL adresy.

## Klíčové body

- Prohlížeč Atlas s integrovaným ChatGPT obsahuje režim "agent", který dokáže autonomně provádět komplexní úkoly jako rezervaci letenek nebo nákup potravin
- Výzkumníci z NeuralTrust objevili, že i adresní řádek (omnibox) prohlížeče je zranitelný vůči útokům prompt injection
- Na rozdíl od předchozích "nepřímých" útoků vyžaduje tato zranitelnost pouze zkopírování podvržené URL adresy uživatelem
- Prohlížeč nevaliduje správně upravené URL a místo toho je interpretuje jako důvěryhodný příkaz od uživatele
- Škodlivé instrukce jsou vykonávány s minimálními bezpečnostními kontrolami, protože systém je považuje za přímý záměr uživatele

## Podrobnosti

Prohlížeč Atlas představuje nový přístup k webovému prohlížení, kde je umělá inteligence ChatGPT integrována přímo do jádra aplikace. Placená verze nabízí "agent mode", který umožňuje prohlížeči autonomně vykonávat celé úkoly - od rezervace služeb až po online nákupy. Tato funkcionalita však s sebou přináší významná bezpečnostní rizika.

Bezpečnostní firma NeuralTrust, která se specializuje na zabezpečení AI agentů, identifikovala zranitelnost přímo v omniboxu - textovém poli v horní části prohlížeče, které přijímá jak URL adresy, tak příkazy v přirozeném jazyce. Softwarový inženýr Martí Jordà vysvětlil, že mírnou úpravou URL adresy lze dosáhnout toho, že prohlížeč ji nevaliduje jako webovou adresu, ale místo toho "zachází s celým obsahem jako s příkazem".

Problém spočívá v tom, že prohlížeč interpretuje obsah takto upravené URL jako důvěryhodný záměr uživatele, což znamená, že škodlivé instrukce jsou vykonávány s "elevovanou důvěrou" a s mnohem menšími bezpečnostními kontrolami. Jordà poznamenal, že "vložené instrukce jsou nyní interpretovány jako důvěryhodný záměr uživatele s menším počtem bezpečnostních kontrol."

Tato zranitelnost se liší od dříve demonstrovaných útoků, kdy výzkumníci vkládali škodlivé příkazy přímo do webových stránek nebo dokumentů. Například jeden výzkumník dokázal přimět prohlížeč, aby místo shrnutí Google Docs dokumentu vypsal text "Trust No AI". Nově objevená zranitelnost je však potenciálně nebezpečnější, protože využívá mechanismus, který uživatelé běžně používají - kopírování a vkládání URL adres.

## Proč je to důležité

Objevení této zranitelnosti poukazuje na fundamentální problém integrace velkých jazykových modelů do kritických aplikací, jako jsou webové prohlížeče. Zatímco AI agenti slibují revoluci v produktivitě a automatizaci úkolů, jejich schopnost vykonávat příkazy s vysokou úrovní autonomie vytváří nové bezpečnostní vektory, které tradiční prohlížeče nemusely řešit.

Pro OpenAI, které se snaží etablovat jako lídr v oblasti AI produktů, představuje tato zranitelnost významný problém důvěryhodnosti. Atlas byl představen jako vlajková loď nové generace AI-first aplikací, ale rychlé objevení kritických bezpečnostních chyb vyvolává otázky o důkladnosti testování před uvedením na trh. Incident také zdůrazňuje rostoucí význam specializovaných bezpečnostních firem jako NeuralTrust, které se zaměřují specificky na zabezpečení AI systémů - oblast, která se rychle stává kritickou součástí kybernetické bezpečnosti.

---

[Číst původní článek](http://futurism.com/artificial-intelligence/serious-new-hack-openai-ai-browser)

**Zdroj:** 📰 Futurism
