---
categories:
- Apple
- iPhone
- Technologie
excerpt: Apple za pár dní představý nové telefony iPhone a očekává se, že alespoň
  jeden z nich bude vybaven Lidarem. Minimálně proto, že jím je vybaven poslední iPad
  a také proto, že se *to povídá*. K čemu a proč?
layout: post
summary_points:
- Apple brzy představí nové iPhony, pravděpodobně s Lidarem.
- Lidar využívá světelný paprsek k měření vzdálenosti v reálném čase.
- Lidar v telefonech zlepší kvalitu fotografií a podpoří augmentovanou realitu.
- Miniaturizace snížila cenu Lidaru pro mobilní zařízení.
title: "K čemu bude LIDAR novým Apple zařízením, zejména iPhone"
---

Apple za pár dní představý nové telefony iPhone a očekává se, že alespoň jeden z nich bude vybaven Lidarem. Minimálně proto, že jím je vybaven poslední iPad a také proto, že se „to povídá“. K čemu a proč?

## K čemu další senzory?

Vzpomínám si, jak jsem před deseti lety, když iPhone slavnostně přidal elektronický kompas, popisoval, k čemu něco takového může být. Tehdy se to zdálo být zbytečné: telefon měl GPSku, k čemu kompas. Zcela zásadní to bylo překvapivě právě pro navigaci, neboť se dalo zjistit ihned, jakým směrem se „telefon dívá“ a nemuseli jste to nekvalitně odvozovat z dat o pohybu přes GPS. Tohle vyrovnalo moje  [tehdejší výhrady ke GPS](filipika-proti-gpskam-a-technickym-blbostem-vubec), které byly opravdu nepoužitelné. Za patnáct let se situace radikálně změnila díky tomu, že se do mobilů doplnily technologie, jako je AGPS, digitální kompas, předinstalované mapové podklady a hlavně rychlá data umožňující kdykoliv mapové podklady stáhnout či doplnit.

Další senzory tedy mají smysl. Možná ještě přesně nevíme, k čemu, ale mají. A tady je jedna z těch vizí.

## Co je to LIDAR

Lidar je obecně něco jako radar, jen místo rádiového signálu  _(odtud RAdar)_  je emitován signál světelný  _(odtud LIdar – Light)_. Může to být paprsek ve viditelném spektru, ale mnohem praktičtější je paprsek v infračerveném spektru, který není lidským okem vidět. Zbavíte se tím nepříjemného stroboskopického blikání Lidaru, respektive okem neuvidíte, ale třeba přes digitální fotoaparát ano. Lidar, podobně jako radar, počítá dobu odrazu paprsku světla od předmětu, na který narazí. No a protože světlo je dost rychlé, umí tak činit vlastně v reálném čase.

K čemu to? Proč používat Lidar a ne třeba kameru, který by mohla vyhodnocovat vzdálenost  [přes paralaxu](https://cs.wikipedia.org/wiki/Paralaxa)?

K tomu odpovím příkladem automobilů Tesla. Ty nejsou Lidarem vybavené, mají „pouze“ kamery. Hlavní výhoda je zřejmá, je to podstatně levnější. Kvalitní Lidar s dosahem potřebným pro automobil stojí mnoho tisíc dolarů (cca 10 000 USD), zatímco i velmi dobré kamery stojí zlomek. Jenže kamery nejsou schopné vnímat prostor. Elon Musk byl při představení svého systému Computer Vision velmi uštěpačný k Lidarům, prý jsou v koncích. Zlaté oči. Systém Vision se snaží dělat to, co lidské oči a mozek: popsat na základě bitmapy obrazu to, co na obrazu je. Jenže dvojice lidských očí dává jakés-takés prostorové vidění a i když se to Tesla snaží překonat, stále jej nemá tak dobré. Pokud jedete Teslou s asistentem řízení po dálnici a v určitém protisvětle se přiblížíte k mostu, kde je náhle stín, začne Tesla ostře brzdit, protože si stín splete se zdí. Lidar by tohle odhalil, od přechodu světla-stín by se paprsek neodrazil a bylo by jasné, že jde jen o stín. Zastánci Tesly samozřejmě připomínají, že podobnou vadou trpí i lidské oko. Lidský mozek ovšem usoudí, že pod dálničním mostem nebude napříč vozovkou postavená zeď a řidič vjede do situace i s rizikem, které si Tesla nemůže dovolit. Nechci tady ovšem zabíhat do rozdílu mezi přístupem Tesla Vision a Lidaru, jsou zde samozřejmě jiné výhody, které uznávám, například Vision narozdíl od Lidaru pozná, že to, co je na silnici, je nafouknutý plastový sáček a ne kámen.

Elon Musk k tématu kamery versus Lidar, kdyby vás to zajímalo…

_Základním benefitem Lidaru je tedy to, že vidí prostorově, vnímá hloubku. Naopak narozdíl od kamery nevnímá barvy._

## Drahý versus levný Lidar

Asi vás napadá otázka, jak to asi Apple chce udělat, že nacpe Lidar za deset tisíc dolarů do telefonu s desetinovou prodejní cenou. Plus tedy ten rozměr.

Inu, odpovědí je tradičně miniaturizace a jiné zadání. Lidar v autě musí vidět dopředu desítky a spíše stovky metrů a sledovat musí minimálně 64 objektů v reálném čase, což vyžaduje kvalitní a dobře dimenzované komponenty. Lidar v iPhone/iPadu je uvažován jako detekce prostoru v místnosti, tedy s dosahem do deseti metrů. Nikdo nepočítá s tím, že si jej přiděláte gumičkou na palubní desku své Fábie a tím z ní uděláte autonomně se pohybující automobil.

Základní rozdíl je tedy v dosahu a v množství bodů, scén a objektů, které umí Lidar v mobilním telefonu obsáhnout. Lidar v automobilu je naprogramovaný tak, aby držel na dohled objekty, čili se při scanování zaměřuje na objekty a neřeší pozadí. Zhustí matici bodů tam, kde vytuší prostorový objekt a neustále kontroluje, zda se objekt pohybuje a kam. To potřebuje k tomu, aby počítač automobilu vyhodnotil kolizní kurz. Takový lidar je mimochodem schopný dodat hmotovou kostru takových objektů, protože se na ně zaměří a „osahá si je“ paprskem. To mimo jiné proto, aby byl schopen vyhodnotit, zda z objektu něco nečouhá, co by mohlo být pro váš vůz kolizní. Barvy samozřejmě ignoruje.

![](/assets/Sni%CC%81mek-obrazovky-2020-10-11-v-15.18.16-1024x722.png)

Takhle si může hloubkově analyzovat scénu Lidar…

Lidar v mobilu jen scanuje celou scénu a podle toho vnímá hloubku umístění prvků, které jsou pevně rozmístěné po scéně. Je významně matematicky jednoduší a především nepotřebuje tak dobrý emitor paprsku ani senzor. Což sráží jeho cenu.

## Rozdíl mezi Lidarem a FaceID systémem TrueDepth

Ještě malý úkrok bokem: iPhone X přinesl FaceID s vestavěnou „3D kamerou“. Ta má zajistit nemožnost hacknutí FaceID přes obyčenou fotku, kterou podržíte před čočkou kamery, jak se stávalo tehdejším Samsungům (a Android telefonům). Ty s vlastní verzí FaceID přispěchaly chvíli před iPhone X, protože se proláklo, na čem Apple pracuje, jenže telefony neměly senzor hloubky a šlo je obejít právě i jen placatou fotkou. Prostorová kamera v iPhone X se jmenuje TrueDepth – a je dobrá, ale je ještě výrazně jednodušší, než Lidar pro mobilní telefony. TrueDepth kamera si nejprve senzorem blízkosti založeným na technologii 3D dToF (Direct Time of Flight – čas letu paprsku, autorem je ST Microelectronics) zjistí, zda je v blízkosti objekt. Pokud ano, udělá kamera fotku a vygeneruje v jediném záblesku 30 000 infrateček do prostoru. Spočítá si dobu jejich návrat, tedy čas, kdy je znovu zachytí na senzororu. Jde o [technologii nazývanou VCSEL](https://www.ametek-ecp.com/resources/blog/2019/february/what-is-a-vcsel)  (Vertical Cavity Surface Emitting Laser).

![](/assets/35133-64123-infrared-dots-ifixit-xl-1024x571.jpg)

Porovnání hustoty měřících bodů Lidaru iPadu a TrueDepth kamery iPhone

Do firmy Finisar, která pro Apple TrueDepth kamery vyrábí, mimochodem musel v roce 2017 Apple investovat přes 390 milionů dolarů, aby se kamera dala vůbec vyrábět a na projektu spolupracovala ve vysokém utajení celá řada dalších firem. Výsledkem jsou tři generace FaceID technologie, kde kamera kamera s vysokou prostorovou rozlišitelností a dosahem max 50 centimetrů je schopná detekovat a vyhodnotit tvář během zlomku vteřiny.

## Co třeba Samsung DepthVision

Samsung do nových telefonů Galaxy S20+ a S20 Ultra přišel s prostorovým systémem DepthVision, což je kamera systému ToF (Time of Flight), která vytvoří jeden záblesk infrabodů a spočítá jejich vzdálenost. Je to o něco jednodušší, než FaceID TrueDepth, ale má to větší dosah. Levné je to především proto, že jde o jeden záblesk, takový emitor se levněji vyrábí – a také senzor vyhodnocuje návrat ze série snímků, i v tom případě jde o výrazně levnější senzor. Vypadá to podobně, jako klasický Lidar, ale je to jednodušší, levnější a zatím s tím nemůžete dělat triky jako je soustředění se na jeden objekt.

_Konec úkroku stranou._

## Lidar v iPhone a iPadu

Lidar systém v iPhone 12 Pro a iPad Pro 2020 je opět založený na technologii ToF/VCSEL, emituje větší skupinu bodů, ovšem postupně, kdy speciální pole „pálí“ jeden bod za bodem v nanosekundových odstupech. Senzor umístěný vedle emitoru vyhodnocuje dobu návratu bodů a je schopen spočítat vzdálenost. Vše se pak v Apple čipu zkombinuje z fotografií a teoreticky je tak možné dělat dobrá kouzla s hloubkou ostrosti a zaostřením.

![](/assets/Apple-iPad-Pro-LiDAR-Opening-Cross-Section_System_Plus_Consulting-1024x576.jpg)

Takhle vypadá čip Lidaru v iPhone Pro 2020.

Dodavatelem Lidaru pro iPad je Sony a jeho pracovní vzdálenost je až pět metrů.

## K čemu tedy Lidar v telefonech?

Chvíli to trvalo, než se dostaneme přes nutné technické vysvětlení k tomu, na co by Lidar v mobilech mohl být.

**Tak především: kvalitnější fotky.**  Díky Lidaru může fotoaparát vědět, jak daleko předmět je a jak se mění jeho hloubka. Kouzla s proměnlivou hloubkou ostrosti, která dříve možná nebyla, najednou možná jsou a fotoaplikace v mobilech tak dohánějí i větší digitální fotoaparáty DSLR. Při focení Lidar zlepší ostření v nekvalitních světelných podmínkách. A je také možné zlepšit efekt bokeh tím, že umožní oddělení objektů pod pozadí.

![](/assets/porovnani-typu-senzoru-sony.png)

Sony ukazuje přínos zkombinování dat z CMOS a Lidar senzorů.

**Za druhé velký přínos bude v Augmentované realitě (AR).** Například IKEA aplikace, která se na dnešním iPhone snaží odhadnout, kam by asi tak mohla na scéně plácnout váš kus nábytku, už bude zcela přesně vědět, co je v popředí a co v pozadí. Už bude vědět dost přesně, co a kam umístit. Je to maličkost, ale pro věrozhodnost, použitelnost a tím i pro rozšíření AR je to důležité. Mimochodem, říká se, že Lidar obsahují i prototypy Apple brýlí, na které firma stále ještě nezanevřela.

![](/assets/ikea-place-hero.jpeg)

Augmentovaná realita v IKEA aplikaci

A s augmentovanou realitou souvisí i **třetí přínos, využitelnost v navigaci**. Apple má patent, který naznačuje použití Lidaru v mobilu s propojením s navigací, kdy telefon hlídá jak kolizní předměty, tak správnou jízdu v pruhu. Dlužno říct, že s dosahem Lidaru cca 5 metrů to je spíše informativní a rozhodně od takového zařízení nemůžete čekat nic většího. Rozhodně se ale Lidar bude hodit pro navigaci uvnitř objektů.

![](/assets/ToF-iPhone-3D-Navigation.jpg)

Na fotku stačí vestavěná kamera, ale pro detekci objektů a kolizí se Lidar hodí. Pamatujte ovšem na omezení dosahu…

Nejsmutnější na takových článcích psaných pár dní před oficiálním oznámením produktu je to, že se zpravidla seknou. A Apple jistě ukáže pár dalších zajímavých využití Lidaru, která by mne nenapadla, nebo bych nevěřil tomu, že jsou použitelná.

Jedna z vizí už nepokrytě počítá s rozjetou sítí 5G a rychlou výměnou dat. Ačkoliv dosah Lidaru je pět metrů, bylo by možné s dostatečným množstvím mobilních telefonů vybavených Lidarem a připojených přes 5G pořizovat v reálném čase 3D plány měst a ty následně využívat. Stačí mít mobil připevněný na palubní desce tak, jak je to na patentu Apple. A tam už to začne být zajímavější i pro technické fajnšmekry, které tolik netankuje lepší ostření fotoaparátu v portrétním režimu…