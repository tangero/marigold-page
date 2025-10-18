---
author: Patrick Zandl
categories:
- Marigold
layout: post
post_excerpt: Chcete do svého prohlížeče dostat notifikaci o tom, že na Marigold.cz vyšel nový článek? V pravém dolním rohu máme ikonku zvonečku, která umožní notifikace zapnout a zase vypnout.
title: Pošleme vám notifikaci o novém článku
thumbnail: https://www.marigold.cz/assets/ikona-notifikace.png
---

Chcete do svého prohlížeče dostat notifikaci o tom, že na Marigold.cz vyšel nový článek? V pravém dolním rohu máme ikonku zvonečku, která umožní notifikace zapnout a zase vypnout. Notifikace vám přijde do otevřeného prohlížeče. 

Notifikace do prohlížeče o novém článku je něco, co nemám příliš rád, protože většinou je to první dialog, co na novém serveru vybafne. Ale zase je to skvělá věc v momentě, kdy server není aktualizován každý den. A to Marigold.cz není. Do vašeho prohlížeče vám přijde notifikace v momentě, kdy se tu objeví nový hlavní článek. Technicky vzato v momentě vystavení nového článku rozesíláme notifikace - zpoždění je minimální. 

**Pozor při používání na telefonech Apple:** iOS vyžaduje, aby byl web přidán na home screen jako web app. Jak na to, se dozvíte na závěr tohoto článku v kapitole _Jak notifikace fungují na mobilních zařízení Apple s iOS_

Notifikace si můžete nastavit také zvláště na [serveru Vibecoding.cz](https://www.vibecoding.cz). 

### Podrobnější vysvětlení

Pro nastavení slouží ikonka zvonečku v pravém dolním rohu obrazovky - umožňuje jen notifikace zapnout a vypnout, jiná nastavení nemáme. 

![Ikona notifikace](https://www.marigold.cz/assets/ikona-notifikace.png)
_Takhle ikonka vypadá, ale tahle nefunguje, jen ta v pravém dolním rohu, neplést s levým dolním rohem..._

#### Doručování pouze do konkrétního prohlížeče

Klíčová informace zní: notifikace se doručí jen do konkrétního prohlížeče, z něhož byla objednána. Každý prohlížeč (Chrome,
Firefox, Safari) nebo dokonce každá jednotlivá instalace prohlížeče na jednom zařízení vytváří vlastní unikátní subscription
endpoint. To znamená, že když si stejný uživatel otevře tvůj web v Chromu a pak ve Firefoxu na stejném počítači, vytvoří se
dvě zcela odlišné subscription. OneSignal je bude považovat za dvě samostatné „zařízení" nebo „hráče" ve svém systému. Když
pošleš notifikaci všem uživatelům, dostane ji uživatel v Chromu i v Firefoxu, ale každý dostane notifikaci ve svém vlastním
prohlížeči – nepůjde tedy o synchronizaci, nýbrž o dvě nezávislé doručení.

#### Nastavení Chrome a synchronizace

Chrome má vestavěnou synchronizaci mezi zařízeními – když se přihlásíš k účtu Google v různých počítačích, Chrome
synchronizuje hesla, bookmarky a další data. Avšak webové push notifikace nejsou součástí synchronizace Chromového účtu.
Subscription endpoint v OneSignal je vázán na konkrétní instalaci prohlížeče na konkrétním zařízení, nikoliv na Googleův
účet. To znamená, že pokud máš Chrome na notebooku a Chrome na desktop počítači, budou mít dvě zcela oddělené subscription.
Notifikace se pošlou nezávisle do obou prohlížečů, ale nejde o synchronizaci v klasickém smyslu – je to prostě dvakrát
vyslané stejné notifikace do různých míst.

#### Podporované prohlížeče

OneSignal podporuje všechny hlavní moderní prohlížeče: Chrome (na počítačích i Androidu), Firefox (na počítačích i
Androidu), Safari (na macOS a od verze iOS 16.4 také na iPhonech a iPadech – tam jen jako web app na home screenu),
Microsoft Edge (na počítačích i Androidu) a Opera (na počítačích i Androidu). Jediné omezení: prohlížeče v režimu
Incognito/Private Browsing nebo v Guest režimu webové push notifikace nepodporují. Také iOS vyžaduje, aby byl web přidán na
home screen jako web app, běžné prohlížení v Safari na iPhonu notifikace nepodporuje.

## iOS Web Push Setup pro vibecoding.cz

Komplexní průvodce aktivací push notifikací na iOS a iPadOS zařízeních pro web app přidaný na home screen.

### Přehled

Apple přidal podporu web push notifikací v iOS/iPadOS 16.4+ pro webové aplikace přidané na home screen uživatele. Tato funkce funguje přes Safari, Chrome a Edge prohlížeče a otevírá nové možnosti pro engagement s uživateli.

**Důležité**: Na rozdíl od desktopových prohlížečů, iOS vyžaduje, aby byl web přidán jako web app na home screen. Běžné browsování v Safari notifikace nepodporuje.

### Systémové požadavky

- **iOS/iPadOS 16.4 nebo vyšší**
- **HTTPS** - vibecoding.cz běží na HTTPS ✅
- **Web Application Manifest** - `manifest.json` ✅
- **Service Worker** - OneSignal SDK ✅
- **Responzivní design** ✅

### Jak notifikace fungují na mobilních zařízení Apple s iOS

#### Architektura

Web push na iOS funguje následovně:

1. Uživatel navštíví vibecoding.cz na Safari, Chrome nebo Edge
2. Uživatel klikne na **Sdílení** a vybere **Přidat na home screen**
3. Web app se uloží na home screen
4. Uživatel otevře app z home screenu (nikoliv z prohlížeče!)
5. App zaregistruje Service Worker a OneSignal SDK
6. Uživatel klikne na tlačítko "Odebírat aktuality"
7. Objeví se nativní iOS prompt pro povolení notifikací
8. Po schválení bude uživatel dostávat notifikace

#### Klíčový rozdíl oproti ostatním zařízením

Na desktopech (Windows, macOS, Linux) se permission prompt objevuje automaticky na základě OneSignal nastavení.

Na iOS **musí být uživatel v rámci web appu** přidaného na home screen a **musí sám iniciovat** permission prompt kliknutím na naše tlačítko.

### Krok za krokem pro uživatele

Níže je návod, který by měl vidět uživatel na vibecoding.cz.

#### Krok 1: Otevři web na iOS

- Jdi na **https://www.vibecoding.cz/ nebo https://www.marigold.cz/**
- Používej Safari, Chrome nebo Edge
- Měla by to být nejnovější verze (iOS 16.4+)

<img src="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='200' height='400'%3E%3Crect fill='%23f0f0f0' width='200' height='400'/%3E%3Ctext x='100' y='200' text-anchor='middle' font-size='14' fill='%23999'%3EiPhone screen: vibecoding.cz otevřeno%3C/text%3E%3C/svg%3E" alt="iPhone screen">

#### Krok 2: Klikni na Sdílení (Share)

- Najdi ikonu **Sdílení** v dolní lišté (vypadá jako obdélník se šipkou)
- Na Androidu je to obdélník s šipkou nahoru
- Klikni na ni

<img src="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='200' height='100'%3E%3Crect fill='%23f0f0f0' width='200' height='100'/%3E%3Ctext x='100' y='50' text-anchor='middle' font-size='12' fill='%23999'%3ESdílení menu%3C/text%3E%3C/svg%3E" alt="Share menu">

#### Krok 3: Vyberi "Přidat na home screen"

V menu, které se objeví, hledej možnost:
- **"Přidat na home screen"** (Safari/Chrome)
- Nebo **"Instalovat"** (Edge)

Posuň si menu dolů, pokud je skrytá.

<img src="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='200' height='200'%3E%3Crect fill='%23f0f0f0' width='200' height='200'/%3E%3Ctext x='100' y='100' text-anchor='middle' font-size='12' fill='%23999'%3E%22Přidat na home screen%22%3C/text%3E%3C/svg%3E" alt="Add to Home Screen option">

### Krok 4: Potvrď název a přidej

Aplikace se zeptá na název. Ponech **"Vibecoding"** nebo zadej vlastní.

Klikni **Přidat** nebo **OK**.

App se nyní zobrazí na home screenu.

#### Krok 5: Otevři app z home screenu

**DŮLEŽITÉ!** Musíš app otevřít z home screenu, ne z prohlížeče!

- Najdi ikonu **Vibecoding** na home screenu
- Klikni na ni
- App se otevře v full-screen režimu (bez prohlížečové lišty nahoře)

App se bude chovat jako nativní aplikace, nikoliv jako web v prohlížeči.

#### Krok 6: Přihlas se k odběru notifikací

Když je app otevřena z home screenu:

- Měl by se zobrazit **modrý button "Odebírat aktuality"** v dolním pravém rohu
- Klikni na něj
- Na 3. návštěvě se může zobrazit i **slidedown prompt** s otázkou

#### Krok 7: Schvál notifikace

Když klikneš na subscribe button, iOS se tě zeptá:

**"Chcete dovolit vibecoding.cz posílat vám notifikace?"**

- Klikni **"Povolit"** (Allow)
- V iOS nastavení se objeví notifikace jako povolená pro tuto web app

#### Hotovo! ✅

Nyní budeš dostávat notifikace o nových AI nástrojích na vibecoding.cz.

Notifikace se budou zobrazovat v:
- **Notification Center** (tažení dolů z horní lišty)
- **Lock Screenu** (když je phone zamčený)
- **Na home screenu** (badge s počtem)

### Troubleshooting

#### Tlačítko "Přidat na home screen" nevidím

- Používáš Safari, Chrome nebo Edge?
- Je tvůj iOS aspoň 16.4?
- Je webová stránka přístupná přes HTTPS? (vibecoding.cz je ✅)
- Zkus otevřít v Safarim (má nejlepší podporu)

#### Povolení se nezobrazuje

**Nejčastější problém:** Jsi v prohlížeči, ne v web appu!

- Ujisti se, že používáš app z home screenu
- App se musí otevřít v **standalone režimu** (bez prohlížečové lišty)
- Na home screenu by měla být ikona s názvem "Vibecoding"

Pokud jsi app smazal(a) z home screenu a přidáš ji znovu:
- Jdi do Nastavení → Safari/Chrome/Edge → Vymaž cache
- Smaž app z home screenu
- Přidej ji znovu

#### Notifikace se neposílají

1. Zkontroluj, že máš notifikace povolené:
   - Nastavení → Vibecoding (v sekci Aplikace)
   - Ujisti se, že jsou zapnuty

2. Zkontroluj OneSignal audience:
   - Jdi na https://onesignal.com/
   - Otevři vibecoding projekt
   - Zkontroluj, že máš abonenty v Audience sekci

3. Zkontroluj server:
   - Jsou notifikace opravdu poslány?
   - Zkontroluj OneSignal Activity log

#### Permission je "denied" a nemohu se odhlásit

Pokud si omylem klikneš "Nepovolit":

1. Smaž app z home screenu
2. Vymaž cache: Nastavení → Safari/Chrome/Edge → Vymaž cache
3. Přidej app znovu
4. Tentokrát vyber "Povolit"