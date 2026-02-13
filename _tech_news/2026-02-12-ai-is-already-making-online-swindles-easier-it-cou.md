---
author: Marisa Aigen
category: kyberbezpečnost
date: '2026-02-12 11:00:00'
description: Anton Cherepanov objevil na VirusTotal soubor s ransomware PromptLock,
  který využívá velké jazykové modely (LLM) k plné automatizaci útoku. Ačkoli se ukázalo,
  že jde o výzkumný projekt, demonstruje to potenciál AI pro flexibilní malware.
importance: 5
layout: tech_news_article
original_title: AI is already making online swindles easier. It could get much worse.
people:
- Anton Cherepanov
publishedAt: '2026-02-12T11:00:00+00:00'
slug: ai-is-already-making-online-swindles-easier-it-cou
source:
  emoji: 🎓
  id: null
  name: MIT Technology Review
title: Umělá inteligence už usnadňuje online podvody. Může to být ještě horší.
url: https://www.technologyreview.com/2026/02/12/1132386/ai-already-making-online-swindles-easier/
urlToImage: https://wp.technologyreview.com/wp-content/uploads/2026/02/opener-final1_social.jpg?resize=1200,600
urlToImageBackup: https://wp.technologyreview.com/wp-content/uploads/2026/02/opener-final1_social.jpg?resize=1200,600
---

## Souhrn
Výzkumníci Anton Cherepanov a Peter Strýček objevili na platformě VirusTotal vzorek ransomware nazvaný PromptLock, který integruje velké jazykové modely (LLM) do všech fází útoku. Tento malware autonomně generuje kód, mapuje systém, šifruje data a píše personalizované výkupné poznámky. Později se ukázalo, že jde o experiment z New York University, nikoli skutečný útok ve volné přírodě.

## Klíčové body
- PromptLock využívá LLM k real-time generování kódu, mapování počítače a tvorbě personalizovaných ransom notes.
- Malware funguje plně autonomně bez lidského zásahu a mění chování při každém spuštění, což ztěžuje detekci.
- Objev vedl k globální mediální pozornosti, ale byl vyvrácen jako výzkumný projekt NYU.
- Ukazuje rizika zneužití generativní AI v kybernetických útocích.

## Podrobnosti
Anton Cherepanov, výzkumník v kyberbezpečnosti, průběžně monitoruje nahrané soubory na VirusTotal, platformě sloužící k analýze potenciálně škodlivého software, jako jsou viry a malware. Koncem srpna minulého roku narazil na nevinně vypadající soubor, který spustil jeho vlastní detekční nástroje. Společně s kolegem Petrem Strýčkem soubor prozkoumali a zjistili, že obsahuje ransomware – typ malware, který šifruje soubory na obětním systému a blokuje je, dokud útočník nedostane výkupné, obvykle v kryptoměnách.

Co tento případ odlišovalo, bylo použití velkých jazykových modelů (LLM), jako jsou ty založené na architektuře podobné GPT. Po instalaci se PromptLock připojil k LLM, aby v reálném čase generoval přizpůsobený kód pro specifické úkoly. Například autonomně prohledal systém, identifikoval citlivá data k enkódování nebo krádeži a na základě obsahu souborů vytvořil personalizované výkupné zprávy – například zmínil konkrétní názvy dokumentů nebo typy dat. Každé spuštění probíhalo jinak díky dynamické generaci, což zvyšuje odolnost vůči antivirovým systémům založeným na signaturách.

Cherepanov a Strýček, kteří pracují pro firmu specializovanou na analýzu malware, tento objev označili za průlomový a publikovali blogový příspěvek, kde ho prezentovali jako první příklad ransomware poháněného AI. Zpráva rychle získala mezinárodní pozornost v médiích jako Wired nebo cybersecurity blogy. Dne následující tým z New York University (NYU) přiznal autorství: šlo o proof-of-concept výzkum, který měl prokázat možnost plné automatizace útoků pomocí LLM. Studenti a výzkumníci z NYU tak simulovali scénář, kde AI nahrazuje manuální práci hackerů, což umožňuje rychlejší a adaptivnější útoky.

Tento případ ilustruje, jak dostupné LLM – jako ty od OpenAI nebo open-source alternativy – lze integrovat do malware přes API volání. Útočník nemusí psát složitý kód; stačí zadat příkaz typu „vygeneruj skript pro šifrování souborů v složce X". To snižuje bariéru pro amatérské hackery a zvyšuje riziko sofistikovaných kampaní.

## Proč je to důležité
Objev PromptLock nastoluje novou éru v kyberbezpečnosti, kde generativní AI umožňuje malware stát se dynamickým a obtížně detekovatelným. I když tento případ byl výzkumný, ukazuje reálný potenciál pro budoucí hrozby: autonomní ransomware by mohl obcházet tradiční obranu, jako jsou heuristické analyzátory, a přizpůsobovat se specifickým cílům firem nebo jednotlivců. Pro průmysl to znamená nutnost rozšířit detekci o analýzu LLM volání v síti a chování v reálném čase. V širším kontextu AI ekosystému to podtrhuje rizika otevřených modelů – bez lepšího guardrailingu (bezpečnostních mechanismů) se stanou nástrojem pro zločin. Firmy jako ESET nebo Kaspersky, kde Cherepanov a Strýček působí, nyní testují obranu proti takovým hybridním hrozbám. Pokud se technologie rozšíří, může vést k eskalaci online podvodů, kde AI generuje nejen kód, ale i phishing e-maily nebo deepfake hlasy pro sociální inženýrství. (512 slov)

---

[Číst původní článek](https://www.technologyreview.com/2026/02/12/1132386/ai-already-making-online-swindles-easier/)

**Zdroj:** 🎓 MIT Technology Review
